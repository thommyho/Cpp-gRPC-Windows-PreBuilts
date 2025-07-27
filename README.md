# Prebuilt binaries gRPC C++ for Windows

### gRPC [v1.74.0](https://github.com/grpc/grpc/releases/tag/v1.74.0)

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
| [v1.74.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.74.0) | [3e7a4d5](https://github.com/grpc/grpc/commit/3e7a4d52d257990fa5b9d80f69f4a591178d9d7c) | Wednesday, July 23, 2025 | 🛠️ Debug<br>🚀 Release<br>🔧 RelWithDebInfo | 💻 MSVC143: x86, x64<br>🖥️ MSVC142: x86, x64<br>🔲 MSVC141: x86, x64 | ✅      |

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

| Third Party Component | Version      | Commit                                                                                                                    | Link                                                                               | Timestamp                   |
| --------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------- |
| abseil-cpp            | 20250512.1   | [76bb243](https://github.com/abseil/abseil-cpp.git/commit/76bb24329e8bf5f39704eb10d21b9a80befa7c81)                       | [abseil-cpp](https://github.com/abseil/abseil-cpp.git)                             | Tuesday, June 17, 2025      |
| benchmark             | v1.9.0       | [12235e2](https://github.com/google/benchmark/commit/12235e24652fc7f809373e7c11a5f73c5763fc4c)                            | [benchmark](https://github.com/google/benchmark)                                   | Friday, August 16, 2024     |
| bloaty                | No tag       | [60209eb](https://github.com/google/bloaty.git/commit/60209eb1ccc34d5deefb002d1b7f37545204f7f2)                           | [bloaty](https://github.com/google/bloaty.git)                                     | Monday, August 16, 2021     |
| boringssl-with-bazel  | No tag       | [c63fadb](https://github.com/google/boringssl.git/commit/c63fadbde60a2224c22189d14c4001bbd2a3a629)                        | [boringssl-with-bazel](https://github.com/google/boringssl.git)                    | Monday, April 21, 2025      |
| cares/cares           | cares-1_19_1 | [6360e96](https://github.com/c-ares/c-ares.git/commit/6360e96b5cf8e5980c887ce58ef727e53d77243a)                           | [cares/cares](https://github.com/c-ares/c-ares.git)                                | Monday, May 22, 2023        |
| envoy-api             | No tag       | [4de3c74](https://github.com/envoyproxy/data-plane-api.git/commit/4de3c74cf21a9958c1cf26d8993c55c6e0d28b49)               | [envoy-api](https://github.com/envoyproxy/data-plane-api.git)                      | Tuesday, January 28, 2025   |
| googleapis            | No tag       | [fe8ba05](https://github.com/googleapis/googleapis.git/commit/fe8ba054ad4f7eca946c2d14a63c3f07c0b586a0)                   | [googleapis](https://github.com/googleapis/googleapis.git)                         | Monday, August 19, 2024     |
| googletest            | v1.17.0      | [52eb810](https://github.com/google/googletest.git/commit/52eb8108c5bdec04579160ae17225d66034bd723)                       | [googletest](https://github.com/google/googletest.git)                             | Wednesday, April 30, 2025   |
| opencensus-proto      | v0.3.0       | [4aa53e1](https://github.com/census-instrumentation/opencensus-proto.git/commit/4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89) | [opencensus-proto](https://github.com/census-instrumentation/opencensus-proto.git) | Monday, July 20, 2020       |
| opentelemetry         | v0.10.0      | [60fa875](https://github.com/open-telemetry/opentelemetry-proto.git/commit/60fa8754d890b5c55949a8c68dcfd7ab5c2395df)      | [opentelemetry](https://github.com/open-telemetry/opentelemetry-proto.git)         | Friday, July 30, 2021       |
| protobuf              | v4.31.1      | [74211c0](https://github.com/protocolbuffers/protobuf.git/commit/74211c0dfc2777318ab53c2cd2c317a2ef9012de)                | [protobuf](https://github.com/protocolbuffers/protobuf.git)                        | Wednesday, May 28, 2025     |
| protoc-gen-validate   | v1.0.4       | [32c2415](https://github.com/envoyproxy/protoc-gen-validate.git/commit/32c2415389a3538082507ae537e7edd9578c64ed)          | [protoc-gen-validate](https://github.com/envoyproxy/protoc-gen-validate.git)       | Wednesday, January 17, 2024 |
| re2                   | 2022-04-01   | [0c5616d](https://github.com/google/re2.git/commit/0c5616df9c0aaa44c9440d87422012423d91c7d1)                              | [re2](https://github.com/google/re2.git)                                           | Wednesday, March 30, 2022   |
| xds                   | No tag       | [3a472e5](https://github.com/cncf/xds.git/commit/3a472e524827f72d1ad621c4983dd5af54c46776)                                | [xds](https://github.com/cncf/xds.git)                                             | Thursday, November 16, 2023 |
| zlib                  | No tag       | [f1f503d](https://github.com/madler/zlib/commit/f1f503da85d52e56aae11557b4d79a42bcaa2b86)                                 | [zlib](https://github.com/madler/zlib)                                             | Monday, January 29, 2024    |
| opentelemetry-cpp     | v1.19.0      | [ced7986](https://github.com/open-telemetry/opentelemetry-cpp/commit/ced79860f8c8a091a2eabfee6d47783f828a9b59)            | [opentelemetry-cpp](https://github.com/open-telemetry/opentelemetry-cpp)           | Wednesday, January 22, 2025 |

### Feedback

For suggestions or issues, feel free to open a ticket in the respective repositories:

- Prebuilt binaries: [gRPC Windows](https://github.com/thommyho/gRPC_windows).
- Visual Studio Examples: [Cpp-gRPC-Visual-Studio-Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples).

______________________________________________________________________

Thank you for using gRPC for C++ on Windows!
