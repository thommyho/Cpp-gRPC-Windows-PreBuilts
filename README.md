# Prebuilt binaries gRPC C++ for Windows

##### Current stable build of gRPC v1.63.0

##### gRPC [v1.63.0](https://github.com/grpc/grpc/releases/tag/v1.63.0)

> They can be downloaded separately as zip archives from the  [releases](https://github.com/thommyho/gRPC_windows/releases) page

##### Releases

| Version                                                                 | Commit                                   | Debug                   | Release                 | RelWithDebInfo          | MSVC143 32Bit           | MSVC143 64Bit           | MSVC142 32 Bit          | MSVC142 64 Bit          | Example                 |
|-------------------------------------------------------------------------|------------------------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| [1.63.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.63.0) | ac1418547838ab067a02af4402046f7bc1cbc44c | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check: |

Build instructions from here: <https://github.com/grpc/grpc/blob/master/BUILDING.md>

Examples included. Tested with VS2019, VS2022 Enterprise and msvc142, msvc143 (Win 10, SDK 10.0)

#### Information about Build system and Tools

| Operating System | SDK Version |
|------------------|-------------|
| Windows 10 (x64) | 10.0        |

| Build Tool | Version     |
|------------|-------------|
| nasm       | 2.15.05     |
| cmake      | 3.23.1      |
| golang     | 1.19        |
| MSVC 142   | 19.29.30143 |
| MSVC 143   | 19.31.31107 |

#### gRPC c++ Third Party Components

| Third Party Component | Version    | Commit                                   | Link                                                         |
|-----------------------|------------|------------------------------------------|--------------------------------------------------------------|
| abseil-cpp            |            | 4a2c63365eff8823a5221db86ef490e828306f9d | <https://github.com/abseil/abseil-cpp>                       |
| benchmark             |            | 344117638c8ff7e239044fd0fa7085839fc03021 | <https://github.com/google/benchmark>                        |
| bloaty                |            | 60209eb1ccc34d5deefb002d1b7f37545204f7f2 | <https://github.com/google/bloaty>                           |
| boringssl-with-bazel  |            | e14d29f68c2d1b02e06f10c83b9b8ea4d061f8df | <https://github.com/google/boringssl>                        |
| cares                 |            | 6360e96b5cf8e5980c887ce58ef727e53d77243a | <https://github.com/c-ares/c-ares>                           |
| envoy-api             |            | 78f198cf96ecdc7120ef640406770aa01af775c4 | <https://github.com/envoyproxy/data-plane-api>               |
| googleapis            |            | 2f9af297c84c55c8b871ba4495e01ade42476c92 | <https://github.com/googleapis/googleapis>                   |
| googletest            |            | 2dd1c131950043a8ad5ab0d2dda0e0970596586a | <https://github.com/google/googletest>                       |
| libuv                 |            | 02a9e1be252b623ee032a3137c0b0c94afbe6809 | <https://github.com/libuv/libuv>                             |
| opencensus-proto      |            | 4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89 | <https://github.com/census-instrumentation/opencensus-proto> |
| opentelemetry         |            | 4bd64c9a336fd438d6c4c9dad2e6b61b0585311f | <https://github.com/open-telemetry/opentelemetry-proto>      |
| protobuf              |            | 2434ef2adf0c74149b9d547ac5fb545a1ff8b6b5 | <https://github.com/google/protobuf>                         |
| protoc-gen-validate   |            | fab737efbb4b4d03e7c771393708f75594b121e4 | <https://github.com/envoyproxy/protoc-gen-validate>          |
| re2                   |            | 0c5616df9c0aaa44c9440d87422012423d91c7d1 | <https://github.com/google/re2>                              |
| xds                   |            | 3a472e524827f72d1ad621c4983dd5af54c46776 | <https://github.com/cncf/xds>                                |
| zlib                  |            | 09155eaa2f9270dc4ed1fa13e2b4b2613e6e4851 | <https://github.com/madler/zlib>                             |

#### Directory Setup for using/testing the provided HelloWorld-Example(s)

```console
.
+-- vs2022
|   +-- 0_HelperScripts
|   +-- 1_HelloWorld_Client
|   +-- 1_HelloWorld_Server
|   +-- 2_HelloWorld_Client_Callback
|   +-- 2_HelloWorld_Server_Callback
|   +-- 3_HelloWorld_Client_Async_1
|   +-- 3_HelloWorld_Client_Async_2
|   +-- 3_HelloWorld_Server_Async
|   +-- 4_HelloWorld_Client_Compression
|   +-- 4_HelloWorld_Server_Compression
|   +-- 5_HelloWorld_Client_Load_Balancing
|   +-- 5_HelloWorld_Server_Load_Balancing
|   +-- 6_HelloWorld_Client_Meta
|   +-- 6_HelloWorld_Server_Meta
|   +-- 7_KeyValueStore_Client
|   +-- 7_KeyValueStore_Server
|   +-- 8_Route_Guide_Client
|   +-- 8_Route_Guide_Server
|   +-- 9_Route_Guide_Client_Callback
|   +-- 9_Route_Guide_Server_Callback
|   +-- protos
|   +-- res
|   +-- Examples_vs2022.sln
+-- vs2019
|   +-- 0_HelperScripts
|   +-- 1_HelloWorld_Client
|   +-- 1_HelloWorld_Server
|   +-- 2_HelloWorld_Client_Callback
|   +-- 2_HelloWorld_Server_Callback
|   +-- 3_HelloWorld_Client_Async_1
|   +-- 3_HelloWorld_Client_Async_2
|   +-- 3_HelloWorld_Server_Async
|   +-- 4_HelloWorld_Client_Compression
|   +-- 4_HelloWorld_Server_Compression
|   +-- 5_HelloWorld_Client_Load_Balancing
|   +-- 5_HelloWorld_Server_Load_Balancing
|   +-- 6_HelloWorld_Client_Meta
|   +-- 6_HelloWorld_Server_Meta
|   +-- 7_KeyValueStore_Client
|   +-- 7_KeyValueStore_Server
|   +-- 8_Route_Guide_Client
|   +-- 8_Route_Guide_Server
|   +-- 9_Route_Guide_Client_Callback
|   +-- 9_Route_Guide_Server_Callback
|   +-- protos
|   +-- res
|  -> + Legacy Examples 2015 and 2017
# Extract the prebuilt bins and libs like this for your disired toolchain e.g.:
+-- MSVC143_64
|   +-- Debug
|       +-- bin
|       +-- cmake
|       +-- include
|       +-- lib
|       +-- share
|   +-- Release
|       +-- bin
|       +-- cmake
|       +-- include
|       +-- lib
|       +-- share
|   +-- RelWithDebInfo
|       +-- bin
|       +-- cmake
|       +-- include
|       +-- lib
|       +-- share
+-- MSVC143_32 ...
+-- MSVC142_64 ...
+-- MSVC142_32 ...
```
