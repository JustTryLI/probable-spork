# AnimePet

AnimePet 是一个二次元桌宠项目，结合了 AI 对话功能，让你的桌面拥有一个可爱的二次元伙伴。

## 功能特性

- 二次元角色动画
- 🤖 AI 对话与互动
-  音效与语音
- 对外 API 接口
-  可配置的角色设定

## 项目结构

```
AnimePet-main/ 
 ├── README.md               # 项目介绍、展示、使用方法 
 ├── main.py                 # 桌宠主程序（入口） 
 ├── api_server.py            # AI + 对外 API 服务 
 ├── config.py                # 配置文件（AI模型、角色设定） 
 ├── requirements.txt         # 依赖列表（pip安装） 
 ├── assets/                  # 资源文件夹 
 │   ├── sprites/             # 二次元帧动画（待机、走路、表情） 
 │   ├── sounds/              # 音效、语音 
 │   └── icons/                # 图标 
 ├── core/                    # 核心逻辑 
 │   ├── ai.py                 # AI 对话、记忆、prompt 
 │   ├── pet.py                # 桌宠状态、情绪、动作 
 │   └── animation.py           # 动画播放 
 └── examples/                 # API调用示例 
     └── api_test.py 
```

## 安装与使用

1. 克隆项目到本地
2. 安装依赖：`pip install -r requirements.txt`
3. 配置 `config.py` 中的 AI 模型和角色设定
4. 运行桌宠：`python main.py`
5. 启动 API 服务：`python api_server.py`

## 配置说明

在 `config.py` 文件中，你可以配置以下内容：

- AI 模型选择与参数
- 角色设定（性格、背景等）
- 动画与音效设置
- API 服务端口

## API 接口

项目提供了 RESTful API 接口，可以通过 `api_server.py` 启动服务，支持以下功能：

- 发送消息给桌宠
- 获取桌宠状态
- 控制桌宠动作

详细 API 文档请参考 `examples/api_test.py` 示例。

## 资源说明

- **sprites/**：存放角色的帧动画图片
- **sounds/**：存放音效和语音文件
- **icons/**：存放应用图标

## 开发计划

- 支持更多角色选择
- 添加更多动画与互动效果
- 优化 AI 对话体验
- 支持自定义角色创建

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
