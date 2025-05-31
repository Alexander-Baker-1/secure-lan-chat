## [1.3.1](https://github.com/Alexander-Baker-1/secure-lan-chat/compare/v1.3.0...v1.3.1) (2025-05-31)


### Bug Fixes

* remove npm plugin from semantic-release config 🔧 ([bd06c0c](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/bd06c0c68dffede95d7b99d8196702573dcbd2ae))

# [1.3.0](https://github.com/Alexander-Baker-1/secure-lan-chat/compare/v1.2.0...v1.3.0) (2025-05-31)


### Features

* **security:** move AES key and encryption logic into secure closure ([1ad7f16](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/1ad7f16537939c5dc14148b53d370cf12de29ed5))

# 📦 Changelog

All notable changes to this project will be documented here.

---

## [1.2.0](https://github.com/Alexander-Baker-1/secure-lan-chat/compare/v1.1.1...v1.2.0) (2025-05-31)

### Features

- test automatic version bump ([b6837f4](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/b6837f4b507666f8e618aef40f79d639a52d40d0))
- test automatic version bump ([776622d](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/776622d4fec51145bc1e9220b23b3ca59e8bc7db))

---

## [1.1.1](https://github.com/Alexander-Baker-1/secure-lan-chat/compare/v1.1.0...v1.1.1) (2025-05-31)

### Bug Fixes

- fetch full git history for tagging in GitHub Actions 🛠️ ([325b688](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/325b688617a36eb39e80daf400f8ccfd757452da))
- fetch remote tags before auto-tagging ([7dc8938](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/7dc8938b2999b4c42a3723a9b00f843d9306e5ed))
- grant write permission to GitHub Actions for tagging ✍️ ([35dba08](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/35dba08ddd64fcdf379fbe0d38d5999f586c2449))
- handle missing initial tags in autotag workflow ([a22f299](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/a22f2997f639ddae16d45d3c1982afa1c35afee8))
- unshallow fetch for tag detection ([09af168](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/09af1685b87eed5378ed0f96f1eadb9df749a804))
- unshallow fetch for tag detection ([26dbe7f](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/26dbe7f41861cf6803b878eef3869d20ad27c99d))
- upgrade Node.js version for semantic-release compatibility 🧠 ([adca53b](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/adca53b5f1af9ca58a82989ced7923c2dba48736))

---

## [1.1.0](https://github.com/Alexander-Baker-1/secure-lan-chat/compare/v1.0.0...v1.1.0) (2025-05-30)

### Security

- Switched from AES-ECB to AES-CBC for encryption
- Added proper IV handling for secure message transmission

### Fixes

- Improved error handling and browser console logging
