# Prebuilt binaries gRPC C++ for Windows

##### Current stable build of gRPC v1.46.7

##### gRPC [v1.46.7](https://github.com/grpc/grpc/releases/tag/v1.46.7)

> They can be downloaded separately as zip archives from the [releases](https://github.com/thommyho/gRPC_windows/releases) page

##### Releases

| Version                                                                  | Commit                                   | Commit-Date               | Debug                   | Release                 | RelWithDebInfo          | MSVC143 32Bit           | MSVC143 64Bit           | MSVC142 32 Bit          | MSVC142 64 Bit          | Example                 |
| ------------------------------------------------------------------------ | ---------------------------------------- | ------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| [v1.46.7](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.7) | 02384e39185f109bd299eb8482306229967dc970 | 2023-02-15 08:24:10+08:00 | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: |

Build instructions from here: <https://github.com/grpc/grpc/blob/master/BUILDING.md>

Examples included. Tested with msvc142, msvc143 (Win 10, SDK 10.0)

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

| Visual Studio Version | Compiler Set Versions    |
| --------------------- | ------------------------ |
| 2022                  | 14.29.30133, 14.41.34120 |
| 2019                  | 14.29.30133              |

#### gRPC c++ Third Party Components

| Third Party Component | Version        | Commit                                   | Link                                                             | Timestamp                 |
| --------------------- | -------------- | ---------------------------------------- | ---------------------------------------------------------------- | ------------------------- |
| zlib                  | v1.2.13        | 04f42ceca40f73e2978b50e93806c2a18c1281fc | <https://github.com/madler/zlib>                                 | 2022-10-13 12:06:55+07:00 |
| protobuf              | v3.19.5        | b464cfbee18c71c40e761a5273ad369f3547294b | <https://github.com/protocolbuffers/protobuf.git>                | 2022-09-14 01:34:47+07:00 |
| googletest            | release-1.12.0 | 0e402173c97aea7a00749e825b194bfede4f2e45 | <https://github.com/google/googletest.git>                       | 2022-02-10 08:20:06+08:00 |
| benchmark             | v1.6.1         | 0baacde3618ca617da95375e0af13ce1baadea47 | <https://github.com/google/benchmark>                            | 2021-09-20 08:19:51-01:00 |
| boringssl-with-bazel  | No tag         | 6195bf8242156c9a2fa75702eee058f91b86a88b | <https://github.com/google/boringssl.git>                        | 2023-02-10 19:05:04+00:00 |
| re2                   | 2021-09-01     | 8e08f47b11b413302749c0d8b17a1c94777495d5 | <https://github.com/google/re2.git>                              | 2021-08-31 09:13:56+00:00 |
| cares/cares           | cares-1_17_2   | 6654436a307a5a686b008c1d4c93b0085da6e6d8 | <https://github.com/c-ares/c-ares.git>                           | 2021-07-24 22:44:39+04:00 |
| bloaty                | No tag         | 60209eb1ccc34d5deefb002d1b7f37545204f7f2 | <https://github.com/google/bloaty.git>                           | 2021-08-16 00:36:22+07:00 |
| abseil-cpp            | 20211102.0     | 215105818dfde3174fe799600bb0f3cae233d0bf | <https://github.com/abseil/abseil-cpp.git>                       | 2021-11-03 19:26:14+04:00 |
| envoy-api             | No tag         | 9c42588c956220b48eb3099d186487c2f04d32ec | <https://github.com/envoyproxy/data-plane-api.git>               | 2022-03-30 19:19:15+00:00 |
| googleapis            | No tag         | 2f9af297c84c55c8b871ba4495e01ade42476c92 | <https://github.com/googleapis/googleapis.git>                   | 2021-07-31 04:40:34+07:00 |
| libuv                 | v1.37.0        | 02a9e1be252b623ee032a3137c0b0c94afbe6809 | <https://github.com/libuv/libuv.git>                             | 2020-04-19 20:15:57+04:00 |
| opencensus-proto      | v0.3.0         | 4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89 | <https://github.com/census-instrumentation/opencensus-proto.git> | 2020-07-20 19:46:08-10:00 |
| opentelemetry         | v0.10.0        | 60fa8754d890b5c55949a8c68dcfd7ab5c2395df | <https://github.com/open-telemetry/opentelemetry-proto.git>      | 2021-07-30 00:27:50-04:00 |
| xds                   | No tag         | cb28da3451f158a947dfc45090fe92b07b243bc1 | <https://github.com/cncf/xds.git>                                | 2021-10-12 00:35:35+07:00 |
