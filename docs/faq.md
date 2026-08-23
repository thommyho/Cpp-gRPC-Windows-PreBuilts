# Frequently Asked Questions (FAQ)

## Table of Contents

1. [General Questions](#general-questions)
2. [Installation & Setup](#installation--setup)
3. [Building Examples](#building-examples)
4. [Troubleshooting](#troubleshooting)
5. [Version Compatibility](#version-compatibility)
6. [License & Legal](#license--legal)

---

## General Questions

### What is Cpp-gRPC-Windows-PreBuilts?

Cpp-gRPC-Windows-PreBuilts provides precompiled gRPC libraries and required header files for Windows development using Visual Studio. It simplifies the setup process by providing ready-to-use archives that can be extracted and used immediately.

### Who should use this project?

This project is ideal for:
- Developers who want to quickly start working with gRPC on Windows
- Teams that need consistent build environments across multiple developers
- Projects requiring support for older Visual Studio versions (2015, 2017)
- Developers who prefer not to compile gRPC from source

### What compilers are supported?

The following Microsoft Visual C++ compiler toolsets are supported:
- **Visual Studio 2022** - MSVC 143
- **Visual Studio 2019** - MSVC 142
- **Visual Studio 2017** - MSVC 141 (up to gRPC v1.45.2)
- **Visual Studio 2015** - MSVC 140 (up to gRPC v1.45.2)

Both 32-bit and 64-bit architectures are supported for all compiler versions.

### What build configurations are available?

Three build configurations are provided:
- **Debug** - For development with full debugging support
- **RelWithDebInfo** - Release builds with debug information (recommended for production)
- **Release** - Optimized builds without debug symbols

---

## Installation & Setup

### How do I download the prebuilt libraries?

You have two options:

1. **Direct from GitHub Releases**: Navigate to the [repository releases page](https://github.com/thommyho/Cpp-gRPC-Windows-PreBuilts/releases) and select your desired gRPC version.

2. **Release Version Table**: Check the available versions in the [release version table](docs/steps.md#release-version-table).

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
└─ MSVC143_64/                # VS2022 64-bit headers/libs
```

### Do I need to install gRPC from source?

**No!** The prebuilt libraries include all necessary components:
- Precompiled `.lib` files for linking
- Required header files (`grpc/`, `protobuf/` directories)
- Visual Studio project examples (pre-configured and debuggable)

---

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

| Example | Description |
|---------|-------------|
| **HelloWorld** | Basic client/server communication |
| **Client Callback / Server Callback** | Asynchronous callback patterns |
| **Async Client/Server** | Modern async implementations |
| **Compression** | gRPC compression support |
| **Load Balancing** | Client-side load balancing |
| **Meta** | Metadata handling examples |
| **KeyValueStore** | Key-value store service |
| **Route Guide** | Complex routing scenarios |

### How do I debug the examples?

The `Debug` and `RelWithDebInfo` configurations include symbol files (`.pdb`) for debugging. Simply:
1. Set breakpoints in your code
2. Run the example with `F5` or use the Debug toolbar
3. Inspect variables, call stacks, and execution flow

---

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

- Check the [setup instructions](docs/steps.md) for detailed installation steps
- Review the [README](../README.md) for an overview and quick start guide
- Create a [GitHub issue](https://github.com/thommyho/Cpp-gRPC-Windows-PreBuilts/issues) for specific problems

---

## Version Compatibility

### Which gRPC versions are available?

| Version | Status | C++ Standard | Examples |
|---------|--------|--------------|----------|
| **1.83.0** | Latest | C++17/20 | ✅ |
| **1.46.7** | Legacy (last C++11) | C++11 | ✅ |
| 1.82.1 - 1.50.0 | Available | C++17/20 | ✅ |
| 1.49.1 - 1.20.0 | Older versions | C++11/14/17 | ✅ |

### What changed in v1.78.1?

Starting with gRPC v1.78.1, the deployment layout for CMake files changed:
- The `cmake` directory was moved from the project root to the `lib` directory
- This change simplifies integration using `find_package`

### Do older Visual Studio versions still work?

Yes! Up to gRPC v1.45.2, support is provided for:
- Visual Studio 2017 (MSVC 141)
- Visual Studio 2015 (MSVC 140)

Note: For the latest gRPC versions (v1.78+), only Visual Studio 2019 and 2022 are supported.

---

## License & Legal

### What license is this project under?

This project is licensed under the **MIT License**. 

### What about the gRPC libraries?

The original gRPC libraries are distributed under the **Apache License 2.0**. Both licenses are compatible, but please ensure you comply with the terms of both when using this software.

### Where can I find complete license information?

Review the following files:
- [LICENSE](../LICENSE) - This project's MIT license
- [THIRD-PARTY-NOTICES.txt](../THIRD-PARTY-NOTICES.txt) - Complete attribution and license information for all third-party components included in gRPC
- [AUTHORS](../AUTHORS) - List of original gRPC contributors

### Can I use this in commercial projects?

Yes! Both the MIT License (for this packaging project) and Apache 2.0 (for gRPC) are permissive licenses that allow commercial use, modification, and distribution with minimal restrictions.

---

## Additional Resources

- [Official gRPC Documentation](https://grpc.io/docs/)
- [gRPC GitHub Repository](https://github.com/grpc/grpc)
- [Official gRPC Windows Prebuilds Repository](https://github.com/thommyho/gRPC_windows)
- [Cpp-gRPC Visual Studio Examples](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples)

---

*Last updated: August 2026*