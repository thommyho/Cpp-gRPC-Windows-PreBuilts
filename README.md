# Prebuilt binaries gRPC C++ for Windows

### gRPC [v1.76.0](https://github.com/grpc/grpc/releases/tag/v1.76.0)

> **Note**: Prebuilt binaries can be downloaded as zip archives from the [Releases](https://github.com/thommyho/gRPC_windows/releases) page.

### Additional Visual Studio Examples

Most C++ examples from the [gRPC repository](https://github.com/grpc/grpc/tree/master/examples/cpp) have been ported to a
Visual Studio-compatible structure. These examples are maintained at [Cpp-gRPC-Visual-Studio-Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples)
and are tested with gRPC versions v1.42.0 and above.

### Documentation

➡️ [Step-by-Step Installation Guide](https://thommyho.github.io/Cpp-gRPC-Windows-PreBuilts) ⬅️

______________________________________________________________________

##### Releases

| Version                                                                  | Commit                                                                                  | Commit-Date                | Build Configurations                        | Compiler Set                                                         | Example |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------- | -------------------------------------------------------------------- | ------- |
| [v1.76.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.76.0) | [f5ffb68](https://github.com/grpc/grpc/commit/f5ffb68d8a2fd603dff16287e90a4ac571e1fec6) | Saturday, October 18, 2025 | 🛠️ Debug<br>🚀 Release<br>🔧 RelWithDebInfo | 💻 MSVC143: x86, x64<br>🖥️ MSVC142: x86, x64<br>🔲 MSVC141: x86, x64 | ✅      |

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
| Processor        | AMD64 Family 26 Model 68 Stepping 0, AuthenticAMD |
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

| Third Party Component | Version    | Commit                                                                                                                    | Link                                                                               | Timestamp                   |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------- |
| abseil-cpp            | 20250512.1 | [76bb243](https://github.com/abseil/abseil-cpp/commit/76bb24329e8bf5f39704eb10d21b9a80befa7c81)                       | [abseil-cpp](https://github.com/abseil/abseil-cpp.git)                             | Tuesday, June 17, 2025      |
| benchmark             | v1.9.0     | [12235e2](https://github.com/google/benchmark/commit/12235e24652fc7f809373e7c11a5f73c5763fc4c)                            | [benchmark](https://github.com/google/benchmark)                                   | Friday, August 16, 2024     |
| bloaty                | No tag     | [60209eb](https://github.com/google/bloaty/commit/60209eb1ccc34d5deefb002d1b7f37545204f7f2)                           | [bloaty](https://github.com/google/bloaty.git)                                     | Monday, August 16, 2021     |
| boringssl-with-bazel  | No tag     | [c63fadb](https://github.com/google/boringssl/commit/c63fadbde60a2224c22189d14c4001bbd2a3a629)                        | [boringssl-with-bazel](https://github.com/google/boringssl.git)                    | Monday, April 21, 2025      |
| cares/cares           | v1.34.5    | [d3a507e](https://github.com/c-ares/c-ares/commit/d3a507e920e7af18a5efb7f9f1d8044ed4750013)                           | [cares/cares](https://github.com/c-ares/c-ares.git)                                | Tuesday, April 08, 2025     |
| envoy-api             | No tag     | [4de3c74](https://github.com/envoyproxy/data-plane-api/commit/4de3c74cf21a9958c1cf26d8993c55c6e0d28b49)               | [envoy-api](https://github.com/envoyproxy/data-plane-api.git)                      | Tuesday, January 28, 2025   |
| googleapis            | No tag     | [fe8ba05](https://github.com/googleapis/googleapis/commit/fe8ba054ad4f7eca946c2d14a63c3f07c0b586a0)                   | [googleapis](https://github.com/googleapis/googleapis.git)                         | Monday, August 19, 2024     |
| googletest            | v1.17.0    | [52eb810](https://github.com/google/googletest/commit/52eb8108c5bdec04579160ae17225d66034bd723)                       | [googletest](https://github.com/google/googletest.git)                             | Wednesday, April 30, 2025   |
| opencensus-proto      | v0.3.0     | [4aa53e1](https://github.com/census-instrumentation/opencensus-proto/commit/4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89) | [opencensus-proto](https://github.com/census-instrumentation/opencensus-proto.git) | Monday, July 20, 2020       |
| opentelemetry         | v0.10.0    | [60fa875](https://github.com/open-telemetry/opentelemetry-proto/commit/60fa8754d890b5c55949a8c68dcfd7ab5c2395df)      | [opentelemetry](https://github.com/open-telemetry/opentelemetry-proto.git)         | Friday, July 30, 2021       |
| protobuf              | v4.31.1    | [74211c0](https://github.com/protocolbuffers/protobuf/commit/74211c0dfc2777318ab53c2cd2c317a2ef9012de)                | [protobuf](https://github.com/protocolbuffers/protobuf.git)                        | Wednesday, May 28, 2025     |
| protoc-gen-validate   | v1.2.1     | [7b06248](https://github.com/envoyproxy/protoc-gen-validate/commit/7b06248484ceeaa947e93ca2747eccf336a88ecc)          | [protoc-gen-validate](https://github.com/envoyproxy/protoc-gen-validate.git)       | Thursday, January 23, 2025  |
| re2                   | 2022-04-01 | [0c5616d](https://github.com/google/re2/commit/0c5616df9c0aaa44c9440d87422012423d91c7d1)                              | [re2](https://github.com/google/re2.git)                                           | Wednesday, March 30, 2022   |
| xds                   | No tag     | [3a472e5](https://github.com/cncf/xds/commit/3a472e524827f72d1ad621c4983dd5af54c46776)                                | [xds](https://github.com/cncf/xds.git)                                             | Thursday, November 16, 2023 |
| zlib                  | No tag     | [f1f503d](https://github.com/madler/zlib/commit/f1f503da85d52e56aae11557b4d79a42bcaa2b86)                                 | [zlib](https://github.com/madler/zlib)                                             | Monday, January 29, 2024    |
| opentelemetry-cpp     | v1.19.0    | [ced7986](https://github.com/open-telemetry/opentelemetry-cpp/commit/ced79860f8c8a091a2eabfee6d47783f828a9b59)            | [opentelemetry-cpp](https://github.com/open-telemetry/opentelemetry-cpp)           | Wednesday, January 22, 2025 |

### Feedback

For suggestions or issues, feel free to open a ticket in the respective repositories:

- Prebuilt binaries: [gRPC Windows](https://github.com/thommyho/gRPC_windows).
- Visual Studio Examples: [Cpp-gRPC-Visual-Studio-Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples).

______________________________________________________________________

Thank you for using gRPC for C++ on Windows!
