# Prebuilt binaries gRPC C++ for Windows

### gRPC [v1.70.1](https://github.com/grpc/grpc/releases/tag/v1.70.1)

> **Note**: Prebuilt binaries can be downloaded as zip archives from the [Releases](https://github.com/thommyho/gRPC_windows/releases) page.

### Additional Visual Studio Examples

Most C++ examples from the [gRPC repository](https://github.com/grpc/grpc/tree/master/examples/cpp) have been ported to a
Visual Studio-compatible structure. These examples are maintained at [Cpp-gRPC-Visual-Studio-Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples)
and are tested with gRPC versions v1.42.0 and above.

### Documentation

➡️ [Step-by-Step Installation Guide](https://thommyho.github.io/Cpp-gRPC-Windows-PreBuilts) ⬅️

______________________________________________________________________

##### Releases

| Version                                                                  | Commit                                                                                  | Commit-Date              | Build Configurations                        | Compiler Set                                                         | Example |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------- | -------------------------------------------------------------------- | ------- |
| [v1.70.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.70.1) | [5e09900](https://github.com/grpc/grpc/commit/5e099002c1600c580ebe1e6741f8ff8b182ffea4) | Friday, January 31, 2025 | 🛠️ Debug<br>🚀 Release<br>🔧 RelWithDebInfo | 💻 MSVC143: x86, x64<br>🖥️ MSVC142: x86, x64<br>🔲 MSVC141: x86, x64 | ✅      |

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
| Windows          | 10.0.22621                                        |
| Processor        | AMD64 Family 23 Model 17 Stepping 0, AuthenticAMD |
| Architecture     | AMD64                                             |

#### Build Tools

| Build Tool | Version |
| ---------- | ------- |
| git        | 2.47.0  |
| cmake      | 3.31.3  |
| nasm       | 2.16.03 |
| golang     | 1.23.5  |

#### Visual Studio Versions and Compiler Sets

| Visual Studio Version | Compiler Set Versions |
| --------------------- | --------------------- |
| 2022                  | 14.42.34433           |
| 2019                  | 14.29.30133           |

#### gRPC c++ Third Party Components

| Third Party Component | Version      | Commit                                                                                                                    | Link                                                                               | Timestamp                    |
| --------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------- |
| abseil-cpp            | 20240722.0   | [4447c75](https://github.com/abseil/abseil-cpp.git/commit/4447c7562e3bc702ade25105912dce503f0c4010)                       | [abseil-cpp](https://github.com/abseil/abseil-cpp.git)                             | Thursday, August 01, 2024    |
| benchmark             | v1.9.0       | [12235e2](https://github.com/google/benchmark/commit/12235e24652fc7f809373e7c11a5f73c5763fc4c)                            | [benchmark](https://github.com/google/benchmark)                                   | Friday, August 16, 2024      |
| bloaty                | No tag       | [60209eb](https://github.com/google/bloaty.git/commit/60209eb1ccc34d5deefb002d1b7f37545204f7f2)                           | [bloaty](https://github.com/google/bloaty.git)                                     | Monday, August 16, 2021      |
| boringssl-with-bazel  | No tag       | [dec0d8f](https://github.com/google/boringssl.git/commit/dec0d8f681348af8bb675e07bd89989665fca8bc)                        | [boringssl-with-bazel](https://github.com/google/boringssl.git)                    | Wednesday, December 11, 2024 |
| cares/cares           | cares-1_19_1 | [6360e96](https://github.com/c-ares/c-ares.git/commit/6360e96b5cf8e5980c887ce58ef727e53d77243a)                           | [cares/cares](https://github.com/c-ares/c-ares.git)                                | Monday, May 22, 2023         |
| envoy-api             | No tag       | [88a3737](https://github.com/envoyproxy/data-plane-api.git/commit/88a37373e3cb5e1ab09e75dfb302b083168e6654)               | [envoy-api](https://github.com/envoyproxy/data-plane-api.git)                      | Monday, January 06, 2025     |
| googleapis            | No tag       | [fe8ba05](https://github.com/googleapis/googleapis.git/commit/fe8ba054ad4f7eca946c2d14a63c3f07c0b586a0)                   | [googleapis](https://github.com/googleapis/googleapis.git)                         | Monday, August 19, 2024      |
| googletest            | v1.15.0      | [2dd1c13](https://github.com/google/googletest.git/commit/2dd1c131950043a8ad5ab0d2dda0e0970596586a)                       | [googletest](https://github.com/google/googletest.git)                             | Friday, October 06, 2023     |
| opencensus-proto      | v0.3.0       | [4aa53e1](https://github.com/census-instrumentation/opencensus-proto.git/commit/4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89) | [opencensus-proto](https://github.com/census-instrumentation/opencensus-proto.git) | Monday, July 20, 2020        |
| opentelemetry         | v0.10.0      | [60fa875](https://github.com/open-telemetry/opentelemetry-proto.git/commit/60fa8754d890b5c55949a8c68dcfd7ab5c2395df)      | [opentelemetry](https://github.com/open-telemetry/opentelemetry-proto.git)         | Friday, July 30, 2021        |
| protobuf              | v3.29.0      | [2d4414f](https://github.com/protocolbuffers/protobuf.git/commit/2d4414f384dc499af113b5991ce3eaa9df6dd931)                | [protobuf](https://github.com/protocolbuffers/protobuf.git)                        | Thursday, November 28, 2024  |
| protoc-gen-validate   | v1.0.4       | [32c2415](https://github.com/envoyproxy/protoc-gen-validate.git/commit/32c2415389a3538082507ae537e7edd9578c64ed)          | [protoc-gen-validate](https://github.com/envoyproxy/protoc-gen-validate.git)       | Wednesday, January 17, 2024  |
| re2                   | 2022-04-01   | [0c5616d](https://github.com/google/re2.git/commit/0c5616df9c0aaa44c9440d87422012423d91c7d1)                              | [re2](https://github.com/google/re2.git)                                           | Wednesday, March 30, 2022    |
| xds                   | No tag       | [3a472e5](https://github.com/cncf/xds.git/commit/3a472e524827f72d1ad621c4983dd5af54c46776)                                | [xds](https://github.com/cncf/xds.git)                                             | Thursday, November 16, 2023  |
| zlib                  | v1.3         | [09155ea](https://github.com/madler/zlib/commit/09155eaa2f9270dc4ed1fa13e2b4b2613e6e4851)                                 | [zlib](https://github.com/madler/zlib)                                             | Friday, August 18, 2023      |
| opentelemetry-cpp     | v1.18.0      | [955a807](https://github.com/open-telemetry/opentelemetry-cpp/commit/955a807c0461544560429c2414b8967f6023e590)            | [opentelemetry-cpp](https://github.com/open-telemetry/opentelemetry-cpp)           | Monday, November 25, 2024    |

### Feedback

For suggestions or issues, feel free to open a ticket in the respective repositories:

- Prebuilt binaries: [gRPC Windows](https://github.com/thommyho/gRPC_windows).
- Visual Studio Examples: [Cpp-gRPC-Visual-Studio-Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples).

______________________________________________________________________

Thank you for using gRPC for C++ on Windows!
