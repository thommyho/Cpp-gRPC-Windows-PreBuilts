# Prebuilt binaries gRPC C++ for Windows

##### Current stable build of gRPC v1.67.1

##### gRPC [v1.67.1](https://github.com/grpc/grpc/releases/tag/v1.67.1)

> They can be downloaded separately as zip archives from the [releases](https://github.com/thommyho/gRPC_windows/releases) page

##### Releases

| Version                                                                  | Commit                                   | Commit-Date                   | Debug                   | Release                 | RelWithDebInfo          | MSVC143 32Bit           | MSVC143 64Bit           | MSVC142 32 Bit          | MSVC142 64 Bit          | Example                 |
|--------------------------------------------------------------------------|------------------------------------------|-------------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| [v1.67.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.67.1) | d3286610f703a339149c3f9be69f0d7d0abb130a | Fri Nov 1 15:48:28 2024 -0700 | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: |

Build instructions from here: <https://github.com/grpc/grpc/blob/master/BUILDING.md>

Examples included. Tested with msvc142, msvc143 (Win 10, SDK 10.0)

#### Information about Build system and Tools

| Operating System | SDK Version     |
|------------------|-----------------|
| Windows          | 10.0.19042.1526 |

| Build Tool | Version     |
|------------|-------------|
| nasm       | 2.15.05     |
| cmake      | 3.23.1      |
| golang     | 1.23.1      |
| MSVC 142   | 14.29.30133 |
| MSVC 143   | 14.41.34120 |

#### gRPC c++ Third Party Components

| Third Party Component | Version | Commit                                   | Link                                                             | Timestamp                      |
|-----------------------|---------|------------------------------------------|------------------------------------------------------------------|--------------------------------|
| abseil-cpp            |         | 4447c7562e3bc702ade25105912dce503f0c4010 | <https://github.com/abseil/abseil-cpp.git>                       | Thu Aug 1 14:05:11 2024 -0400  |
| benchmark             |         | 344117638c8ff7e239044fd0fa7085839fc03021 | <https://github.com/google/benchmark>                            | Thu Aug 31 13:16:50 2023 +0100 |
| bloaty                |         | 60209eb1ccc34d5deefb002d1b7f37545204f7f2 | <https://github.com/google/bloaty.git>                           | Sun Aug 15 10:36:22 2021 -0700 |
| boringssl-with-bazel  |         | b8b3e6e11166719a8ebfa43c0cde9ad7d57a84f6 | <https://github.com/google/boringssl.git>                        | Tue Sep 3 23:53:10 2024 +0000  |
| cares/cares           |         | 6360e96b5cf8e5980c887ce58ef727e53d77243a | <https://github.com/c-ares/c-ares.git>                           | Mon May 22 08:01:44 2023 -0400 |
| envoy-api             |         | f8b75d1efa92bbf534596a013d9ca5873f79dd30 | <https://github.com/envoyproxy/data-plane-api.git>               | Fri Jul 19 16:50:15 2024 +0000 |
| googleapis            |         | fe8ba054ad4f7eca946c2d14a63c3f07c0b586a0 | <https://github.com/googleapis/googleapis.git>                   | Mon Aug 19 07:44:05 2024 -0700 |
| googletest            |         | 2dd1c131950043a8ad5ab0d2dda0e0970596586a | <https://github.com/google/googletest.git>                       | Thu Oct 5 14:13:04 2023 -0700  |
| opencensus-proto      |         | 4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89 | <https://github.com/census-instrumentation/opencensus-proto.git> | Tue Jul 21 15:46:08 2020 +1000 |
| opentelemetry         |         | 60fa8754d890b5c55949a8c68dcfd7ab5c2395df | <https://github.com/open-telemetry/opentelemetry-proto.git>      | Fri Jul 30 08:27:50 2021 +0400 |
| opentelemetry-cpp     |         | 4bd64c9a336fd438d6c4c9dad2e6b61b0585311f | <https://github.com/open-telemetry/opentelemetry-cpp>            | Wed Dec 6 20:39:21 2023 +0100  |
| protobuf              |         | 10ef3f77683f77fb3c059bf47725c27b3ff41e63 | <https://github.com/protocolbuffers/protobuf.git>                | Tue Sep 10 13:36:10 2024 -0700 |
| protoc-gen-validate   |         | 32c2415389a3538082507ae537e7edd9578c64ed | <https://github.com/envoyproxy/protoc-gen-validate.git>          | Tue Jan 16 14:01:04 2024 -0800 |
| re2                   |         | 0c5616df9c0aaa44c9440d87422012423d91c7d1 | <https://github.com/google/re2.git>                              | Wed Mar 30 18:41:25 2022 +0000 |
| xds                   |         | 3a472e524827f72d1ad621c4983dd5af54c46776 | <https://github.com/cncf/xds.git>                                | Thu Nov 16 09:28:03 2023 -0500 |
| zlib                  |         | 09155eaa2f9270dc4ed1fa13e2b4b2613e6e4851 | <https://github.com/madler/zlib>                                 | Fri Aug 18 01:45:36 2023 -0700 |
