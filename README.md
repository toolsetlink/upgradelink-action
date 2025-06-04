# UpgradeLink Action

**UpgradeLink** - [全端支持，一站式应用升级分发平台及解决方案](http://upgrade.toolsetlink.com/)

## 项目简介
此项目为开源的 Tauri 项目，用于快速接入 UpgradeLink 服务。通过在 GitHub Action 中引入此模块，可自动将生成的版本文件和升级任务配置到 UpgradeLink 系统，无需额外手动操作。


## 接入方式
```yaml
  upgradeLink-upload:
    needs:  publish-tauri  # 依赖于publish-tauri作业完成
    runs-on: ubuntu-latest
    steps:
      - name: Send a request to UpgradeLink
        uses: toolsetlink/upgradelink-action@v4
        with:
          source-url: 'https://github.com/toolsetlink/tauri-demo/releases/download/tauri-demo-v${{ needs.publish-tauri.outputs.appVersion }}/latest.json'
          access-key: ${{ secrets.UPGRADE_LINK_ACCESS_KEY }}  # ACCESS_KEY  密钥key
          tauri-key: ${{ secrets.UPGRADE_LINK_TAURI_KEY }}    # TAURI_KEY tauri 应用唯一标识
```


## 完整案例参考
[tauri-demo 示例项目](http://upgrade.toolsetlink.com/)  
（可查看实际部署效果及完整 GitHub Action 配置）


### 配置说明
- **source-url**：需指向包含 Tauri 应用版本信息的 JSON 文件（通常为 Tauri 打包生成的 `latest.json`）
- **access-key**：在 UpgradeLink 平台创建应用后生成的访问密钥，用于身份验证
- **tauri-key**：Tauri 应用在 UpgradeLink 平台的唯一标识，与应用配置绑定


### 最佳实践
1. 在 GitHub 仓库的 **Settings > Secrets** 中配置 `UPGRADE_LINK_ACCESS_KEY` 和 `UPGRADE_LINK_TAURI_KEY`，避免明文暴露密钥
2. 确保 `publish-tauri` 作业已正确生成并上传版本文件
3. 可通过监听 `release` 事件触发此 Action，实现版本发布与升级配置的自动化流程