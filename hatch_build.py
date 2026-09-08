# noqa: INP001
# -*- coding: utf-8 -*-
"""Hatch 构建钩子(已汉化注释)。

在打包 Open WebUI 时由 hatchling 自动调用,
负责先构建前端(npm install + npm run build)。
"""
import os
import shutil
import subprocess
from sys import stderr

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        super().initialize(version, build_data)
        stderr.write('>>> Building Open Webui frontend\n')
        # 在 PATH 中定位 npm;找不到则直接终止构建
        npm = shutil.which('npm')
        if npm is None:
            raise RuntimeError('NodeJS `npm` is required for building Open Webui but it was not found')
        stderr.write('### npm install\n')
        subprocess.run([npm, 'install', '--force'], check=True)  # noqa: S603
        stderr.write('\n### npm run build\n')
        # 把构建版本号写入环境变量,前端会将其嵌入构建产物
        os.environ['APP_BUILD_HASH'] = version
        node_options = os.environ.get('NODE_OPTIONS', '')
        # 确保 Node 堆内存上限为 8GB,避免前端构建时内存不足
        if '--max-old-space-size' not in node_options:
            os.environ['NODE_OPTIONS'] = f'{node_options} --max-old-space-size=8192'.strip()
        subprocess.run([npm, 'run', 'build'], check=True)  # noqa: S603
