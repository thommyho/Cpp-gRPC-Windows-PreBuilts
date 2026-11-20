# Frequently Asked Questions (FAQ)

## Table of Contents

1. [General Questions](#general-questions)
2. [Installation & Setup](#installation-setup)
3. [Building Examples](#building-examples)
4. [Troubleshooting](#troubleshooting)
5. [Version Compatibility](#version-compatibility)
6. [License & Legal](#license-legal)

______________________________________________________________________

## General Questions

### What is Cpp-gRPC-Windows-PreBuilts?

Cpp-gRPC-Windows-PreBuilts provides prebuilt [gRPC C++](https://github.com/grpc/grpc) libraries for Windows and Visual Studio.
You download ready-to-use ZIP archives, extract them, and link against gRPC without building it from source.

Each release contains:

- **Library archives** (for example `MSVC143_64.zip`) with the headers and precompiled libraries for one compiler and one architecture.
- **Examples** (`Examples.zip`) with preconfigured Visual Studio solutions for the official gRPC C++ examples.
- **Build information** that records the compilers, SDKs and settings used for the build (tracked since v1.22.0).

The project is split across these repositories:

| Repository | Content |
| ---------- | ------- |
| [Cpp-gRPC-Windows-PreBuilts](https://github.com/thommyho/Cpp-gRPC-Windows-PreBuilts) | Overview, release table and this documentation |
| [gRPC_windows](https://github.com/thommyho/gRPC_windows/releases) | Release downloads (ZIP archives) |
| [gRPC_windows_prebuilt](https://github.com/thommyho/gRPC_windows_prebuilt) | Build information for each version |
| [Cpp-gRPC-Visual-Studio-Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples) | Source of the Visual Studio examples |

### Who should use this project?

This project is a good fit if you:

- Want to start with gRPC on Windows quickly, without building it from source.
- Need the same gRPC binaries for every developer and every CI agent of a team.
- Use Visual Studio solutions (`.sln`) or CMake with `find_package`.
- Must stay on C++11 or an older Visual Studio version (see [Version Compatibility](#version-compatibility)).

### Which gRPC versions are available?

- **Latest stable build**: [v1.85.3](https://github.com/thommyho/gRPC_windows/releases/tag/v1.85.3)
- **Last build requiring only C++11**: [v1.46.7](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.7)

All available versions, from v1.20.0 up to the latest, are in the [release table](steps.md#download).

### What compilers are supported?

The following Microsoft Visual C++ compiler toolsets are supported:

| Visual Studio | Toolset | gRPC versions |
| ------------- | ------- | ------------- |
| Visual Studio 2026 | MSVC 145 | v1.85.0 and later |
| Visual Studio 2022 | MSVC 143 | all current releases |
| Visual Studio 2019 | MSVC 142 | up to v1.84.x |
| Visual Studio 2017 | MSVC 141 | up to v1.45.1, and v1.46.7 |
| Visual Studio 2015 | MSVC 140 | up to v1.45.x |

Each toolset is available for 32-bit (`x86`) and 64-bit (`x64`).
The [release table](steps.md#download) shows the exact toolsets of each version.

### What build configurations are available?

Each library archive contains three build configurations:

- **Debug** - No optimization, full debug symbols. Use it for development.
- **RelWithDebInfo** - Optimized, with debug symbols. Use it for production builds that you must debug.
- **Release** - Optimized, without debug symbols.

______________________________________________________________________

## Installation & Setup

### How do I download the prebuilt libraries?

You have two options:

1. **Direct from GitHub Releases**: Navigate to the [releases page](https://github.com/thommyho/gRPC_windows/releases) and select your desired gRPC version.

2. **Release Version Table**: Check the available versions in the [release version table](steps.md#download).

### What files should I download?

For each gRPC version, you need to download:

1. **Library archives** (e.g., `MSVC143_64.zip`, `MSVC142_32.zip`) - Contains precompiled `.lib` files and header directories
2. **Examples archive** (`Examples.zip`) - Contains Visual Studio project files for all supported compiler versions

### How do I organize the downloaded files?

Extract all archives into a single project directory with the following structure:

```
your-project/
├─ vs2015/                    # Visual Studio 2015 projects (from Examples.zip)
├─ vs2017/                    # Visual Studio 2017 projects (from Examples.zip)
├─ vs2019/                    # Visual Studio 2019 projects (from Examples.zip)
├─ vs2022/                    # Visual Studio 2022 projects (from Examples.zip)
├─ MSVC140_32/                # VS2015 32-bit headers/libs
├─ MSVC140_64/                # VS2015 64-bit headers/libs
├─ MSVC141_32/                # VS2017 32-bit headers/libs
├─ MSVC141_64/                # VS2017 64-bit headers/libs
├─ MSVC142_32/                # VS2019 32-bit headers/libs
├─ MSVC142_64/                # VS2019 64-bit headers/libs
├─ MSVC143_32/                # VS2022 32-bit headers/libs
├─ MSVC143_64/                # VS2022 64-bit headers/libs
├─ MSVC145_32/                # VS2026 32-bit headers/libs
└─ MSVC145_64/                # VS2026 64-bit headers/libs
```

### Do I need to install gRPC from source?

**No!** The prebuilt libraries include all necessary components:

- Precompiled `.lib` files for linking
- Required header files (`grpc/`, `protobuf/` directories)
- Visual Studio project examples (pre-configured and debuggable)

______________________________________________________________________

## Building Examples

### How do I build the examples in Visual Studio?

1. Open the appropriate solution file:

    - `vs2015/HelloWorld.sln` for Visual Studio 2015
    - `vs2017/HelloWorld.sln` for Visual Studio 2017
    - `vs2019/HelloWorld.sln` for Visual Studio 2019
    - `vs2022/HelloWorld.sln` for Visual Studio 2022

2. Ensure the correct compiler toolset is selected in Visual Studio options

3. Build the solution:

    - Menu: **Build → Build Solution**
    - Shortcut: `Ctrl+Shift+B`

4. The output will be organized as:

    ```
    _out_/
    └─ <architecture>/          # x64 or x86
       └─ <build configuration>/ # Debug, Release, or RelWithDebInfo
          └─ <example binaries>  # executables and resources
    ```

### What examples are available?

Starting from gRPC v1.43.0, the following examples are included:

| Example                               | Description                       |
| ------------------------------------- | --------------------------------- |
| **HelloWorld**                        | Basic client/server communication |
| **Client Callback / Server Callback** | Asynchronous callback patterns    |
| **Async Client/Server**               | Modern async implementations      |
| **Compression**                       | gRPC compression support          |
| **Load Balancing**                    | Client-side load balancing        |
| **Meta**                              | Metadata handling examples        |
| **KeyValueStore**                     | Key-value store service           |
| **Route Guide**                       | Complex routing scenarios         |

### How do I debug the examples?

The `Debug` and `RelWithDebInfo` configurations include symbol files (`.pdb`) for debugging. Simply:

1. Set breakpoints in your code
2. Run the example with `F5` or use the Debug toolbar
3. Inspect variables, call stacks, and execution flow

______________________________________________________________________

## Troubleshooting

### Common Issues

#### "Cannot find module 'grpc'" error

**Cause**: Visual Studio cannot locate the gRPC header files.

**Solution**:

1. Verify that the `grpc/` directory exists in your project root
2. Check that the include paths in your `.vcxproj` file point to the correct locations
3. Ensure you downloaded both library archives and examples archive

#### "MSB8028: No target specified" error

**Cause**: The solution file was opened with an incompatible Visual Studio version.

**Solution**:

1. Close Visual Studio
2. Open the solution with the matching Visual Studio version (e.g., `vs2019/*.sln` with VS 2019)
3. Rebuild the solution

#### "LNK1181: cannot open input file" error

**Cause**: The precompiled library files are missing or in the wrong location.

**Solution**:

1. Verify that all required `.lib` files exist in their respective architecture folders
2. Check that the library path is correctly specified in the project properties
3. Ensure you downloaded archives for both 32-bit and 64-bit if needed

#### "Configuration 'Release' is not available" error

**Cause**: Attempting to build with a configuration that doesn't exist.

**Solution**: Use one of the three supported configurations: `Debug`, `RelWithDebInfo`, or `Release`.

### Where can I find more help?

- Check the [setup instructions](steps.md) for detailed installation steps
- Create a [GitHub issue](https://github.com/thommyho/Cpp-gRPC-Windows-PreBuilts/issues) for specific problems

______________________________________________________________________

## Version Compatibility

### Which C++ standard do I need?

| gRPC version     | Minimum C++ standard |
| ---------------- | -------------------- |
| v1.47.0 and later | C++14 (newer gRPC versions can require a newer standard, see the [gRPC release notes](https://github.com/grpc/grpc/releases)) |
| v1.46.7 and older | C++11 |

gRPC C++ **v1.47.0** is the first release that requires C++14.
If you cannot upgrade to C++14, use **v1.46.7**, the last release that requires only C++11.

### What changed in v1.78.1?

Starting with gRPC v1.78.1, the deployment layout for CMake files changed:

- The `cmake` directory was moved from the project root to the `lib` directory
- This change simplifies integration using `find_package`

### Do older Visual Studio versions still work?

Yes, but only with older gRPC versions:

- Visual Studio 2019 (MSVC 142): up to gRPC v1.84.x
- Visual Studio 2017 (MSVC 141): up to gRPC v1.45.1, and v1.46.7
- Visual Studio 2015 (MSVC 140): up to gRPC v1.45.x

From gRPC v1.85.0, releases are built for Visual Studio 2026 (MSVC 145) and Visual Studio 2022 (MSVC 143).
See [What compilers are supported?](#what-compilers-are-supported) for the full list.

______________________________________________________________________

## License & Legal

### What license is this project under?

This project is licensed under the **MIT License**.

### What about the gRPC libraries?

The original gRPC libraries are distributed under the **Apache License 2.0**. Both licenses are compatible, but please ensure you comply with the terms of both when using this software.

### Where can I find complete license information?

Review the following files:
- [LICENSE](../LICENSE) - This project's MIT license
- [THIRD-PARTY-NOTICES.txt](../THIRD-PARTY-NOTICES.txt) - Complete attribution and license information for all third-party components included in gRPC

### Can I use this in commercial projects?

Yes! Both the MIT License (for this packaging project) and Apache 2.0 (for gRPC) are permissive licenses that allow commercial use, modification, and distribution with minimal restrictions.

______________________________________________________________________

## Additional Resources

- [Official gRPC Documentation](https://grpc.io/docs/)
- [gRPC GitHub Repository](https://github.com/grpc/grpc)
- [Official gRPC Windows Prebuilds Repository](https://github.com/thommyho/gRPC_windows)
- [Cpp-gRPC Visual Studio Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples)

______________________________________________________________________

*Last updated: August 2026*
