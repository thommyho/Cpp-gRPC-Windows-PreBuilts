# Prebuilt binaries gRPC C++ for Windows
##### Current stable build of gRPC v1.41.1
##### gRPC [v1.41.1](https://github.com/grpc/grpc/releases/tag/v1.41.1) 

> They can be downloaded separately as zip archives from the  [releases](https://github.com/thommyho/gRPC_windows/releases) page


##### Releases

| Version | Commit | Debug | Release  | RelWithDebInfo | MSVC142 32Bit | MSVC142 64Bit | MSVC141 32 Bit | MSVC141 64 Bit | MSVC140 32 Bit | MSVC140 64 Bit | Example |
|---------|------------|-------|----------|----------------|---------------|---------------|----------------|----------------|----------------|----------------|---------|
| [1.41.1 ](https://github.com/thommyho/gRPC_windows/releases/tag/v1.41.1) | 635693ce624f3b3a89e5a764f0664958ef08b2b9 | :ballot_box_with_check: | :ballot_box_with_check: | :ballot_box_with_check:              | :ballot_box_with_check:             | :ballot_box_with_check:             | :ballot_box_with_check:              | :ballot_box_with_check:              | :ballot_box_with_check:              | :ballot_box_with_check:              | :ballot_box_with_check:       |

Build instructions from here: https://github.com/grpc/grpc/blob/master/BUILDING.md

HelloWorld-Example included. Tested with VS2015, VS2017 and VS2019 Enterprise and msvc140, msvc141, msvc142 (Win 10, SDK 10.0.19042)

#### Information about Build system and Tools

| Operating System | SDK Version   |
|------------------|---------------|
| Windows 10 (x64) |  10.0.19042   |

| Build Tool       | Version        |
|------------------|----------------|
| nasm             | 2.14.02        |
| cmake            | 3.19.2         |
| golang           | 1.17           |
| MSVC 140         | 19.0.24245.0   |
| MSVC 141         | 19.16.27045.0  |
| MSVC 142         | 19.29.30133.0  |

#### gRPC c++ Third Party Components

| Third Party Component | Version        | Commit                                   | Link                                                       |
|-----------------------|----------------|------------------------------------------|------------------------------------------------------------|
| abseil-cpp            | lts_2020_02_25 | 997aaf3a28308eba1b9156aa35ab7bca9688e9f6 | https://github.com/abseil/abseil-cpp                       |
| benchmark             | v1.5.2         | 73d4d5e8d6d449fc8663765a42aa8aeeee844489 | https://github.com/google/benchmark                        |
| bloaty                |                | 73594cde8c9a52a102c4341c244c833aa61b9c06 | https://github.com/google/bloaty                           |
| benchmark             | v1.5.2         | 73d4d5e8d6d449fc8663765a42aa8aeeee844489 | https://github.com/google/benchmark                        |
| boringssl-with-bazel  |                | 340faef0ad19283e985ce7fff0dec73ba4022c8d | https://github.com/google/boringssl                        |
| cares                 | cares_1_15_0   | e982924acee7f7313b4baa4ee5ec000c5e373c30 | https://github.com/c-ares/c-ares                           |
| envoy-api             |                | 2f0d081fab0b0823f088c6e368f40e1992f46fcd | https://github.com/envoyproxy/data-plane-api               |
| googleapis            |                | 2f9af297c84c55c8b871ba4495e01ade42476c92 | https://github.com/googleapis/googleapis                   |
| googletest            |                | c9ccac7cb7345901884aabf5d1a786cfa6e2f397 | https://github.com/google/googletest                       |
| libuv                 | v1.34.0        | 15ae750151ac9341e5945eb38f8982d59fb99201 | https://github.com/libuv/libuv                             |
| opencensus-proto      | v0.3.0         | 4aa53e15cbf1a47bc9087e6cfdca214c1eea4e89 | https://github.com/census-instrumentation/opencensus-proto |
| protobuf              | v3.17.3        | 909a0f36a10075c4b4bc70fdee2c7e32dd612a72 | https://github.com/google/protobuf                         | 
| protoc-gen-validate   |                | 9da36e59fef2267fc2b1849a05159e3ecdf24f3  | https://github.com/envoyproxy/protoc-gen-validate          |
| re2                   | 2020-06-1      | aecba11114cf1fac5497aeb844b6966106de3eb6 | https://github.com/google/re2                              |
| udpa                  |                | 6414d713912e988471d192940b62bf552b11793a | https://github.com/cncf/udpa                               |
| zlib                  | v1.2.11        | cacf7f1d4e3d44d871b605da3b647f07d718623f | https://github.com/madler/zlib                             |

#### Directory Setup for using/testing the provided HelloWorld-Example(s)

```console
.
+-- vs2015
|   +-- _gen_proto_cpp
|   +-- gRPC_PropertySheet
|       +-- gRPC.props
|   +-- HelloWorld_Client
|       +-- HelloWorld_Client.vcxproj
|       +-- HelloWorld_Client.vcxproj.filters
|       +-- pch.h
|       +-- pch.cpp
|       +-- HelloWorld_Client.cpp
|   +-- HelloWorld_Server
|       +-- HelloWorld_Server.vcxproj
|       +-- HelloWorld_Server.vcxproj.filters
|       +-- pch.h
|       +-- pch.cpp
|       +-- HelloWorld_Server.cpp
|   +-- HelloWorld_vs2015.sln
+-- vs2017
|   +-- _gen_proto_cpp
|   +-- gRPC_PropertySheet
|       +-- gRPC.props
|   +-- HelloWorld_Client
|       +-- HelloWorld_Client.vcxproj
|       +-- HelloWorld_Client.vcxproj.filters
|       +-- pch.h
|       +-- pch.cpp
|       +-- HelloWorld_Client.cpp
|   +-- HelloWorld_Server
|       +-- HelloWorld_Server.vcxproj
|       +-- HelloWorld_Server.vcxproj.filters
|       +-- pch.h
|       +-- pch.cpp
|       +-- HelloWorld_Server.cpp
|   +-- HelloWorld_vs2017.sln
+-- vs2019
|   +-- _gen_proto_cpp
|   +-- gRPC_PropertySheet
|       +-- gRPC.props
|   +-- HelloWorld_Client
|       +-- HelloWorld_Client.vcxproj
|       +-- HelloWorld_Client.vcxproj.filters
|       +-- pch.h
|       +-- pch.cpp
|       +-- HelloWorld_Client.cpp
|   +-- HelloWorld_Server
|       +-- HelloWorld_Server.vcxproj
|       +-- HelloWorld_Server.vcxproj.filters
|       +-- pch.h
|       +-- pch.cpp
|       +-- HelloWorld_Server.cpp
|   +-- HelloWorld_vs2019.sln
# Extract the prebuilt bins and libs like this for your disired toolchain e.g.:
+-- MSVC142_64
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
+-- MSVC142_32 ...
+-- MSVC141_64 ...
+-- MSVC141_32 ...
+-- MSVC140_64 ...
+-- MSVC140_32 ...
```
