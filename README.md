# Prebuilt binaries gRPC C++ for Windows

##### Current stable build of gRPC v1.46.7

##### gRPC [v1.46.7](https://github.com/grpc/grpc/releases/tag/v1.46.7)

> **Note**: Prebuilt binaries can be downloaded as zip archives from the [Releases](https://github.com/thommyho/gRPC_windows/releases) page.

### Additional Visual Studio Examples

Most C++ examples from the [gRPC repository](https://github.com/grpc/grpc/tree/master/examples/cpp) have been ported to a
Visual Studio-compatible structure. These examples are maintained at [Cpp-gRPC-Visual-Studio-Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples)
and are tested with gRPC versions v1.42.0 and above.

### Documentation

➡️ [Step-by-Step Installation Guide](https://thommyho.github.io/Cpp-gRPC-Windows-PreBuilts) ⬅️

______________________________________________________________________

##### Releases

| Version                                                                  | Commit                                                                                  | Commit-Date                  | Build Configurations                        | Compiler Set                                                         | Example |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | ---------------------------- | ------------------------------------------- | -------------------------------------------------------------------- | ------- |
| [v1.46.7](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.7) | [02384e3](https://github.com/grpc/grpc/commit/02384e39185f109bd299eb8482306229967dc970) | Wednesday, February 15, 2023 | 🛠️ Debug<br>🚀 Release<br>🔧 RelWithDebInfo | 💻 MSVC143: x86, x64<br>🖥️ MSVC142: x86, x64<br>🔲 MSVC141: x86, x64 | ✅      |

______________________________________________________________________

### Explanation of Symbols

- **Build Configurations**:
  - 🛠️ Debug: Development configuration with debugging symbols.
  - 🚀 Release: Optimized for production use.
  - 🔧 RelWithDebInfo: Combination of optimizations and debugging symbols.
- **Compiler Sets**:
  - 💻 MSVC143: Visual Studio 2022 (x86/x64).
  - 🖥️ MSVC142: Visual Studio 2019 (x86/x64).
  - 🔲 MSVC141: Visual Studio 2017 (x86/x64) --> Discontinued from v1.45.2.

______________________________________________________________________

Build instructions from here: <https://github.com/grpc/grpc/blob/master/BUILDING.md>

Examples included. Tested with msvc142, msvc143 (Win 10, SDK 10.0)

______________________________________________________________________

#### Information about Build system and Tools

| Operating System | SDK Version                                       |
| ---------------- | ------------------------------------------------- |
| Windows          | 10.0                                              |

#### Build Tools

| Build Tool | Version |
| ---------- | ------- |
| git        | 2.47.1  |
| cmake      | 3.30.5  |
| nasm       | 2.16.03 |
| golang     | 1.23.2  |

#### Visual Studio Versions and Compiler Sets

| Visual Studio Version | Compiler Set Versions    |
| --------------------- | ------------------------ |
| 2022                  | 19.31.31107              |
| 2019                  | 19.29.30143              |

#### gRPC c++ Third Party Components

| Third Party Component | Version        | Commit                                                                                                                    | Link                                                                               | Timestamp                     |
| --------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------- |
| zlib                  | v1.2.13        | [04f42ce](https://github.com/madler/zlib/commit/04f42ceca40f73e2978b50e93806c2a18c1281fc)                                 | [zlib](https://github.com/madler/zlib)                                             | Thursday, October 13, 2022    |
| protobuf              | v3.19.5        | [b464cfb](https://github.com/protocolbuffers/protobuf.git/commit/b464cfbee18c71c40e761a5273ad369f3547294b)                | [protobuf](https://github.com/protocolbuffers/protobuf.git)                        | Wednesday, September 14, 2022 |
| googletest            | release-1.12.0 | [0e40217](https://github.com/google/googletest.git/commit/0e402173c97aea7a00749e825b194bfede4f2e45)                       | [googletest](https://github.com/google/googletest.git)                             | Thursday, February 10, 2022   |
| benchmark             | v1.6.1         | [0baacde](https://github.com/google/benchmark/commit/0baacde3618ca617da95375e0af13ce1baadea47)                            | [benchmark](https://github.com/google/benchmark)                                   | Monday, September 20, 2021    |
| boringssl-with-bazel  | No tag         | [6195bf8](https://github.com/google/boringssl.git/commit/6195bf8242156c9a2fa75702eee058f91b86a88b)                        | [boringssl-with-bazel](https://github.com/google/boringssl.git)                    | Friday, February 10, 2023     |
| re2                   | 2021-09-01     | [8e08f47](https://github.com/google/re2.git/commit/8e08f47b11b413302749c0d8b17a1c94777495d5)                              | [re2](https://github.com/google/re2.git)                                           | Tuesday, August 31, 2021      |
| cares/cares           | cares-1_17_2   | [6654436](https://github.com/c-ares/c-ares.git/commit/6654436a307a5a686b008c1d4c93b0085da6e6d8)                           | [cares/cares](https://github.com/c-ares/c-ares.git)                                | Saturday, July 24, 2021       |
| bloaty                | No tag         | [60209eb](https://github.com/google/bloaty.git/commit/60209eb1ccc34d5deefb002d1b7f37545204f7f2)                           | [bloaty](https://github.com/google/bloaty.git)                                     | Monday, August 16, 2021       |
| abseil-cpp            | 20211102.0     | [2151058](https://github.com/abseil/abseil-cpp.git/commit/215105818dfde3174fe799600bb0f3cae233d0bf)                       | [abseil-cpp](https://github.com/abseil/abseil-cpp.git)                             | Wednesday, November 03, 2021  |
| envoy-api             | No tag         | [9c42588](https://github.com/envoyproxy/data-plane-api.git/commit/9c42588c956220b48eb3099d186487c2f04d32ec)               | [envoy-api](https://github.com/envoyproxy/data-plane-api.git)                      | Wednesday, March 30, 2022     |
| googleapis            | No tag         | [2f9af29](https://github.com/googleapis/googleapis.git/commit/2f9af297c84c55c8b871ba4495e01ade42476c92)                   | [googleapis](https://github.com/googleapis/googleapis.git)                         | Saturday, July 31, 2021       |
| libuv                 | v1.37.0        | [02a9e1b](https://github.com/libuv/libuv.git/commit/02a9e1be252b623ee032a3137c0b0c94afbe6809)                             | [libuv](https://github.com/libuv/libuv.git)                                        | Sunday, April 19, 2020        |
| opencensus-proto      | v0.3.0         | [4aa53e1](https://github.com/census-instrumentation/opencensus-proto.git/commit/4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89) | [opencensus-proto](https://github.com/census-instrumentation/opencensus-proto.git) | Monday, July 20, 2020         |
| opentelemetry         | v0.10.0        | [60fa875](https://github.com/open-telemetry/opentelemetry-proto.git/commit/60fa8754d890b5c55949a8c68dcfd7ab5c2395df)      | [opentelemetry](https://github.com/open-telemetry/opentelemetry-proto.git)         | Friday, July 30, 2021         |
| xds                   | No tag         | [cb28da3](https://github.com/cncf/xds.git/commit/cb28da3451f158a947dfc45090fe92b07b243bc1)                                | [xds](https://github.com/cncf/xds.git)                                             | Tuesday, October 12, 2021     |

### Feedback

For suggestions or issues, feel free to open a ticket in the respective repositories:

- Prebuilt binaries: [gRPC Windows](https://github.com/thommyho/gRPC_windows).
- Visual Studio Examples: [Cpp-gRPC-Visual-Studio-Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples).

______________________________________________________________________

Thank you for using gRPC for C++ on Windows!
