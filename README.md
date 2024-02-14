# CrossCore-Vanilla

将交错战线恢复至初识时香草般的体验：

- 原版登录画面。

- 登录后的加载界面展示原版插画。
- 角色画面显示的跃升等级恢复罗马数字。
- 开启国际服资源加载（`internation.txt` 的~~那个零~~ 0 已修改为 1）。

## 免责声明

虽然本项目所有文件来自官方原版安装包，但使用修改版仍然是官方**不建议**的操作，本项目作者及贡献者不为玩家使用本项目造成的包括数据丢失、账户封禁等任何后果承担任何责任。

## iOS 使用方法

如果之前使用过任何其他补丁包，建议在操作之前删除游戏，重新从 App Store 安装最新版本获得干净的环境避免可能的问题。

1. 在电脑上安装 iMazing（macOS 和 Windows 都支持），使用 iMazing 备份 iOS 设备上的交错战线 app 数据为 `交错战线.imazingapp`。备份及恢复详细操作请自行参考 iMazing 官方文档。
2. 使用任何常见压缩包管理工具将 `Container` 目录加入上一步获得的 `交错战线.imazingapp` 数据包覆盖已有文件。

   例如最常见的命令行 `zip` 工具： `zip -0r 交错战线.imazingapp Container -x '*.DS_Store'`。

   本项目已经刻意使用与数据包内一致的目录结构存储文件，方便覆盖操作。
3. 使用 iMazing 将修改过的 `交错战线.imazingapp` 恢复回 iOS 设备。**务必注意最后在 iOS 上的操作，确保选择“保留部分设置并继续”，并且“不传输任何内容”（不从 iCloud 恢复数据），以免 iOS 设备数据被重置**。
4. 启动游戏，等待更新国际服资源后即可重新获得香草般的体验。

## Android 使用方法

暂缺，欢迎有意愿贡献 Android 使用方法的玩家提交 PR。

## 文件列表

- 登录界面：`videos/login/login*`
- 加载界面插画：`Custom/textures_bigs_uis_bgs_loading_*`
- 包含跃升等级罗马数字的 UI 图标库：`Custom/textures_uis_icons_rolecard_bg`
