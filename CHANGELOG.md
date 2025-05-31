## [1.1.1](https://github.com/Alexander-Baker-1/secure-lan-chat/compare/v1.1.0...v1.1.1) (2025-05-31)


### Bug Fixes

* fetch full git history for tagging in GitHub Actions 🛠️ ([325b688](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/325b688617a36eb39e80daf400f8ccfd757452da))
* fetch remote tags before auto-tagging ([7dc8938](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/7dc8938b2999b4c42a3723a9b00f843d9306e5ed))
* grant write permission to GitHub Actions for tagging ✍️ ([35dba08](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/35dba08ddd64fcdf379fbe0d38d5999f586c2449))
* handle missing initial tags in autotag workflow ([a22f299](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/a22f2997f639ddae16d45d3c1982afa1c35afee8))
* unshallow fetch for tag detection ([09af168](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/09af1685b87eed5378ed0f96f1eadb9df749a804))
* unshallow fetch for tag detection ([26dbe7f](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/26dbe7f41861cf6803b878eef3869d20ad27c99d))
* upgrade Node.js version for semantic-release compatibility 🧠 ([adca53b](https://github.com/Alexander-Baker-1/secure-lan-chat/commit/adca53b5f1af9ca58a82989ced7923c2dba48736))

# 📦 Changelog

All notable changes to this project will be documented here.

---

## [v1.1.0] - 2025-05-30
### 🔐 Security
- Switched from AES-ECB to AES-CBC for encryption
- Added proper IV handling for secure message transmission

### 🛠 Fixes
- Improved error handling and browser console logging

---
