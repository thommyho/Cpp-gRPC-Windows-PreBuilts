# Prebuilt binaries gRPC C++ for Windows

##### Current stable build of gRPC v1.68.2

##### gRPC [v1.68.2](https://github.com/grpc/grpc/releases/tag/v1.68.2)

> They can be downloaded separately as zip archives from the [releases](https://github.com/thommyho/gRPC_windows/releases) page

##### Releases

| Version                                                                  | Commit                                   | Commit-Date               | Debug                   | Release                 | RelWithDebInfo          | MSVC143 32Bit           | MSVC143 64Bit           | MSVC142 32 Bit          | MSVC142 64 Bit          | Example                 |
| ------------------------------------------------------------------------ | ---------------------------------------- | ------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| [v1.68.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.68.2) | 859bc5216ba3955fb8925326bdec391fd93c8730 | 2024-12-04 02:03:35+08:00 | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: |

Build instructions from here: <https://github.com/grpc/grpc/blob/master/BUILDING.md>

Examples included. Tested with msvc142, msvc143 (Win 10, SDK 10.0)

#### Information about Build system and Tools

| Operating System | SDK Version                                       |
| ---------------- | ------------------------------------------------- |
| Windows          | 10.0.22631                                        |

#### Build Tools

| Build Tool | Version |
| ---------- | ------- |
| git        | 2.47.0  |
| cmake      | 3.30.5  |
| nasm       | 2.16.03 |
| golang     | 1.23.2  |

#### Visual Studio Versions and Compiler Sets

| Visual Studio Version | Compiler Set Versions    |
| --------------------- | ------------------------ |
| 2022                  | 14.29.30133, 14.41.34120 |
| 2019                  | 14.29.30133              |

#### gRPC c++ Third Party Components

| Third Party Component | Version      | Commit                                   | Link                                                             | Timestamp                 |
| --------------------- | ------------ | ---------------------------------------- | ---------------------------------------------------------------- | ------------------------- |
| abseil-cpp            | 20240722.0   | 4447c7562e3bc702ade25105912dce503f0c4010 | <https://github.com/abseil/abseil-cpp.git>                       | 2024-08-01 22:05:11+04:00 |
| benchmark             | v1.8.3       | 344117638c8ff7e239044fd0fa7085839fc03021 | <https://github.com/google/benchmark>                            | 2023-08-31 11:16:50-01:00 |
| bloaty                | No tag       | 60209eb1ccc34d5deefb002d1b7f37545204f7f2 | <https://github.com/google/bloaty.git>                           | 2021-08-16 00:36:22+07:00 |
| boringssl-with-bazel  | No tag       | b8b3e6e11166719a8ebfa43c0cde9ad7d57a84f6 | <https://github.com/google/boringssl.git>                        | 2024-09-03 23:53:10+00:00 |
| cares/cares           | cares-1_19_1 | 6360e96b5cf8e5980c887ce58ef727e53d77243a | <https://github.com/c-ares/c-ares.git>                           | 2023-05-22 16:01:44+04:00 |
| envoy-api             | No tag       | f8b75d1efa92bbf534596a013d9ca5873f79dd30 | <https://github.com/envoyproxy/data-plane-api.git>               | 2024-07-19 16:50:15+00:00 |
| googleapis            | No tag       | fe8ba054ad4f7eca946c2d14a63c3f07c0b586a0 | <https://github.com/googleapis/googleapis.git>                   | 2024-08-19 21:44:05+07:00 |
| googletest            | v1.15.0      | 2dd1c131950043a8ad5ab0d2dda0e0970596586a | <https://github.com/google/googletest.git>                       | 2023-10-06 04:13:04+07:00 |
| opencensus-proto      | v0.3.0       | 4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89 | <https://github.com/census-instrumentation/opencensus-proto.git> | 2020-07-20 19:46:08-10:00 |
| opentelemetry         | v0.10.0      | 60fa8754d890b5c55949a8c68dcfd7ab5c2395df | <https://github.com/open-telemetry/opentelemetry-proto.git>      | 2021-07-30 00:27:50-04:00 |
| protobuf              | v3.28.1      | 10ef3f77683f77fb3c059bf47725c27b3ff41e63 | <https://github.com/protocolbuffers/protobuf.git>                | 2024-09-11 03:36:10+07:00 |
| protoc-gen-validate   | v1.0.4       | 32c2415389a3538082507ae537e7edd9578c64ed | <https://github.com/envoyproxy/protoc-gen-validate.git>          | 2024-01-17 06:01:04+08:00 |
| re2                   | 2022-04-01   | 0c5616df9c0aaa44c9440d87422012423d91c7d1 | <https://github.com/google/re2.git>                              | 2022-03-30 18:41:25+00:00 |
| xds                   | No tag       | 3a472e524827f72d1ad621c4983dd5af54c46776 | <https://github.com/cncf/xds.git>                                | 2023-11-16 19:28:03+05:00 |
| zlib                  | v1.3         | 09155eaa2f9270dc4ed1fa13e2b4b2613e6e4851 | <https://github.com/madler/zlib>                                 | 2023-08-18 15:45:36+07:00 |
| opentelemetry-cpp     | v1.13.0      | 4bd64c9a336fd438d6c4c9dad2e6b61b0585311f | <https://github.com/open-telemetry/opentelemetry-cpp>            | 2023-12-06 18:39:21-01:00 |
