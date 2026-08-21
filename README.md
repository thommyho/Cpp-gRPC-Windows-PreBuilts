# Cpp-gRPC-Windows-PreBuilts

## Overview

Prebuilt libraries and required header files packaged in archives for **gRPC** on Windows.

### Highlights

- For several modern Visual Studio Compilers:
  - Visual Studio 2022 - `MSVC 143`
  - Visual Studio 2019 - `MSVC 142`  
  - Visual Studio 2017 - `MSVC 141` - until v1.45.2
  - Visual Studio 2015 - `MSVC 140` - until v1.45.2
- For both **32- and 64-Bit architectures**
- Convenient with all three build configurations: `Release`, `RelWithDebInfo`, `Debug`

### What's Included

- Precompiled gRPC libraries (`.lib` files)
- Required header files (`grpc/`, `protobuf/` directories)
- Ready-to-use Visual Studio project examples from the official gRPC project
  - For Visual Studio 2022, 2019, 2017, and 2015 (up to v1.45.2)
  - **Pre-configured** - Can be used in seconds
  - **Debuggable** - `RelWithDebInfo` and `Debug` configurations include symbols

## Requirements

One of the following compilers:

- Visual Studio 2022 (MSVC 143)
- Visual Studio 2019 (MSVC 142)
- Visual Studio 2017 (MSVC 141) - until v1.45.2
- Visual Studio 2015 (MSVC 140) - until v1.45.2

For a better development experience, use one of the IDEs with the upper-mentioned compilers.

## Download

### Option 1: Direct from GitHub Releases

Navigate to the [repository](https://github.com/thommyho/Cpp-gRPC-Windows-PreBuilts) and select your desired gRPC version on the landing page.

### Option 2: Release Version Table

| Version | Build Info | All Configurations | Examples |
|---------|------------|-------------------|----------|
| **[1.83.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.83.0)** (latest) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.83.0) | ✅ | ✅ |
| **[1.46.7](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.7)** (legacy, last C++11) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.46.7) | ✅ | ✅ |
| 1.82.1 - 1.50.0 | [links available](https://github.com/thommyho/gRPC_windows/releases) | ✅ | ✅ |
| 1.49.1 - 1.20.0 | [older versions](https://github.com/thommyho/gRPC_windows/releases) | ✅ | ✅ |

> **Note:** Starting with v1.78.1, the deployment layout for CMake files has changed. The `cmake` directory has been moved from the project root into the `lib` directory for straightforward integration using `find_package`.

> **Note:** The precompiled libraries are attached as assets (compressed zip archives) to the bottom of each release page.

## Setup Instructions

### Step 1: Download Archives

- [x] Download one or more library archives (e.g., `MSVC143_64.zip`)
- [x] Download the corresponding `Examples.zip` from the same release

### Step 2: Unpack and Organize Files

Extract all downloaded files into a single project directory. The expected structure should look like:

```
your-project/
├─ vs2015/                    # From Examples.zip - Visual Studio 2015 projects
├─ vs2017/                    # From Examples.zip - Visual Studio 2017 projects
├─ vs2019/                    # From Examples.zip - Visual Studio 2019 projects
├─ vs2022/                    # From Examples.zip - Visual Studio 2022 projects
├─ MSVC140_32/                # From library archives - VS2015 32-bit headers/libs
├─ MSVC140_64/                # From library archives - VS2015 64-bit headers/libs
├─ MSVC141_32/                # From library archives - VS2017 32-bit headers/libs
├─ MSVC141_64/                # From library archives - VS2017 64-bit headers/libs
├─ MSVC142_32/                # From library archives - VS2019 32-bit headers/libs
├─ MSVC142_64/                # From library archives - VS2019 64-bit headers/libs
├─ MSVC143_32/                # From library archives - VS2022 32-bit headers/libs
└─ MSVC143_64/                # From library archives - VS2022 64-bit headers/libs
```

### Step 3: Build Examples

#### Using Visual Studio IDE

1. Open the `Examples_<vs_compiler_name>.sln` file with your corresponding Visual Studio version.
2. If everything was correctly placed, no error popup should appear.
3. Click **Build → Build Solution** or use the shortcut `Ctrl+Shift+B` to build all examples.
4. The output will be organized as:
   ```
   _out_/
   └─ <architecture>/          # x64 or x86
      └─ <build configuration>/ # Debug, Release, or RelWithDebInfo
         └─ <example binaries>  # executables and resources
   ```

## Available Examples (from v1.43.0+)

Each Visual Studio directory contains a solution file with multiple examples:

- **HelloWorld** - Basic client/server communication
- **Client Callback / Server Callback** - Asynchronous callback patterns
- **Async Client/Server** - Modern async implementations
- **Compression** - gRPC compression support
- **Load Balancing** - Client-side load balancing
- **Meta** - Metadata handling examples
- **KeyValueStore** - Key-value store service
- **Route Guide** - Complex routing scenarios

## Related Resources

- [Official gRPC Windows Prebuilds Repository](https://github.com/thommyho/gRPC_windows)
- [Cpp-gRPC Visual Studio Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples)
- [gRPC Official Documentation](https://grpc.io/docs/)

## Troubleshooting

For common issues and FAQs, please refer to the [FAQ documentation](docs/faq.md) or create an issue on GitHub.

---

## License & Attribution

This project is licensed under the [MIT License](LICENSE).

### gRPC Upstream Attribution

This project packages prebuilt libraries from the official [gRPC project](https://github.com/grpc/grpc). 
Please review the [THIRD-PARTY-NOTICES.txt](THIRD-PARTY-NOTICES.txt) file for complete attribution
and license information for all third-party components included in gRPC.

The original gRPC project is distributed under the Apache License 2.0, and this packaging effort
is distributed under the MIT License. Both licenses are compatible, but please ensure you comply
with the terms of both when using this software.

**Author**: Thomas Hochstrasser  
**Original gRPC Authors**: See [gRPC contributors](https://github.com/grpc/grpc/blob/master/AUTHORS)
