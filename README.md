# Prebuilt binaries gRPC C++ for Windows

##### Current stable build of gRPC v1.68.1

##### gRPC [v1.68.1](https://github.com/grpc/grpc/releases/tag/v1.68.1)

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
| [v1.68.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.68.1) | [796e87f](https://github.com/grpc/grpc/commit/796e87f16136533977b8647b50a020519fd7a137) | Wednesday, November 27, 2024 | 🛠️ Debug<br>🚀 Release<br>🔧 RelWithDebInfo | 💻 MSVC143: x86, x64<br>🖥️ MSVC142: x86, x64<br>🔲 MSVC141: x86, x64 | ✅      |

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
| Windows          | 10.0.22631                                        |
| Processor        | AMD64 Family 25 Model 97 Stepping 2, AuthenticAMD |
| Architecture     | AMD64                                             |

#### Build Tools

| Build Tool | Version |
| ---------- | ------- |
| git        | 2.47.1  |
| cmake      | 3.30.5  |
| nasm       | 2.16.03 |
| golang     | 1.23.2  |

#### Visual Studio Versions and Compiler Sets

| Visual Studio Version | Compiler Set Versions |
| --------------------- | --------------------- |
| 2022                  | 14.41.34120           |
| 2019                  | 14.29.30133           |

#### gRPC c++ Third Party Components

| Third Party Component | Version      | Commit                                                                                                                    | Link                                                                               | Timestamp                     |
| --------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------- |
| abseil-cpp            | 20240722.0   | [4447c75](https://github.com/abseil/abseil-cpp.git/commit/4447c7562e3bc702ade25105912dce503f0c4010)                       | [abseil-cpp](https://github.com/abseil/abseil-cpp.git)                             | Thursday, August 01, 2024     |
| benchmark             | v1.8.3       | [3441176](https://github.com/google/benchmark/commit/344117638c8ff7e239044fd0fa7085839fc03021)                            | [benchmark](https://github.com/google/benchmark)                                   | Thursday, August 31, 2023     |
| bloaty                | No tag       | [60209eb](https://github.com/google/bloaty.git/commit/60209eb1ccc34d5deefb002d1b7f37545204f7f2)                           | [bloaty](https://github.com/google/bloaty.git)                                     | Monday, August 16, 2021       |
| boringssl-with-bazel  | No tag       | [b8b3e6e](https://github.com/google/boringssl.git/commit/b8b3e6e11166719a8ebfa43c0cde9ad7d57a84f6)                        | [boringssl-with-bazel](https://github.com/google/boringssl.git)                    | Tuesday, September 03, 2024   |
| cares/cares           | cares-1_19_1 | [6360e96](https://github.com/c-ares/c-ares.git/commit/6360e96b5cf8e5980c887ce58ef727e53d77243a)                           | [cares/cares](https://github.com/c-ares/c-ares.git)                                | Monday, May 22, 2023          |
| envoy-api             | No tag       | [f8b75d1](https://github.com/envoyproxy/data-plane-api.git/commit/f8b75d1efa92bbf534596a013d9ca5873f79dd30)               | [envoy-api](https://github.com/envoyproxy/data-plane-api.git)                      | Friday, July 19, 2024         |
| googleapis            | No tag       | [fe8ba05](https://github.com/googleapis/googleapis.git/commit/fe8ba054ad4f7eca946c2d14a63c3f07c0b586a0)                   | [googleapis](https://github.com/googleapis/googleapis.git)                         | Monday, August 19, 2024       |
| googletest            | v1.15.0      | [2dd1c13](https://github.com/google/googletest.git/commit/2dd1c131950043a8ad5ab0d2dda0e0970596586a)                       | [googletest](https://github.com/google/googletest.git)                             | Friday, October 06, 2023      |
| opencensus-proto      | v0.3.0       | [4aa53e1](https://github.com/census-instrumentation/opencensus-proto.git/commit/4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89) | [opencensus-proto](https://github.com/census-instrumentation/opencensus-proto.git) | Monday, July 20, 2020         |
| opentelemetry         | v0.10.0      | [60fa875](https://github.com/open-telemetry/opentelemetry-proto.git/commit/60fa8754d890b5c55949a8c68dcfd7ab5c2395df)      | [opentelemetry](https://github.com/open-telemetry/opentelemetry-proto.git)         | Friday, July 30, 2021         |
| protobuf              | v3.28.1      | [10ef3f7](https://github.com/protocolbuffers/protobuf.git/commit/10ef3f77683f77fb3c059bf47725c27b3ff41e63)                | [protobuf](https://github.com/protocolbuffers/protobuf.git)                        | Wednesday, September 11, 2024 |
| protoc-gen-validate   | v1.0.4       | [32c2415](https://github.com/envoyproxy/protoc-gen-validate.git/commit/32c2415389a3538082507ae537e7edd9578c64ed)          | [protoc-gen-validate](https://github.com/envoyproxy/protoc-gen-validate.git)       | Wednesday, January 17, 2024   |
| re2                   | 2022-04-01   | [0c5616d](https://github.com/google/re2.git/commit/0c5616df9c0aaa44c9440d87422012423d91c7d1)                              | [re2](https://github.com/google/re2.git)                                           | Wednesday, March 30, 2022     |
| xds                   | No tag       | [3a472e5](https://github.com/cncf/xds.git/commit/3a472e524827f72d1ad621c4983dd5af54c46776)                                | [xds](https://github.com/cncf/xds.git)                                             | Thursday, November 16, 2023   |
| zlib                  | v1.3         | [09155ea](https://github.com/madler/zlib/commit/09155eaa2f9270dc4ed1fa13e2b4b2613e6e4851)                                 | [zlib](https://github.com/madler/zlib)                                             | Friday, August 18, 2023       |
| opentelemetry-cpp     | v1.13.0      | [4bd64c9](https://github.com/open-telemetry/opentelemetry-cpp/commit/4bd64c9a336fd438d6c4c9dad2e6b61b0585311f)            | [opentelemetry-cpp](https://github.com/open-telemetry/opentelemetry-cpp)           | Wednesday, December 06, 2023  |

### Feedback

For suggestions or issues, feel free to open a ticket in the respective repositories:

- Prebuilt binaries: [gRPC Windows](https://github.com/thommyho/gRPC_windows).
- Visual Studio Examples: [Cpp-gRPC-Visual-Studio-Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples).

______________________________________________________________________

Thank you for using gRPC for C++ on Windows!
