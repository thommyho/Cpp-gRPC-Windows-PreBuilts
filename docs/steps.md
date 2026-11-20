# Getting started

## Download

- Navigate to the [repository](https://github.com/thommyho/Cpp-gRPC-Windows-PreBuilts)
- On the landing page select your desired gRPC version

Or use following release table

!!! important "C++14 required from v1.47.0"

    gRPC C++ **v1.47.0** is the first release requiring C++14.
    If you cannot upgrade to C++14, use **v1.46.7**, the last release requiring only C++11 support.

!!! danger "Changed CMake layout from v1.78.1"

    Starting with v1.78.1, the deployment layout for the CMake files has changed.
    The `cmake` directory has moved from the project root into the `lib` directory.
    This enables straightforward integration using `find_package` with CMake.

!!! note "Compiler sets"

    - `MSVC145`: Visual Studio 2026 (from v1.85.0)
    - `MSVC143`: Visual Studio 2022
    - `MSVC142`: Visual Studio 2019 (until v1.84.x)
    - `MSVC141`: Visual Studio 2017 (until v1.45.1, and v1.46.7)

| Version | Build-Info | Compiler Set (x86, x64) | All Build-Configurations | Examples |
| :-----: | :--------: | :---------------------: | :----------------------: | :------: |
| **[1.85.3](https://github.com/thommyho/gRPC_windows/releases/tag/v1.85.3) (:octicons-heart-fill-24:{ .heart } latest)** | **[link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.85.3)** | `MSVC145` `MSVC143` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| **[1.84.3](https://github.com/thommyho/gRPC_windows/releases/tag/v1.84.3) (:octicons-heart-fill-24:{ .heart } latest 1.84.x)** | **[link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.84.3)** | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| **[1.46.7](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.7) (:octicons-heart-fill-24:{ .heart } latest C++11)** | **[link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.46.7)** | `MSVC143` `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.85.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.85.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.85.2) | `MSVC145` `MSVC143` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.85.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.85.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.85.1) | `MSVC145` `MSVC143` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.85.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.85.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.85.0) | `MSVC145` `MSVC143` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.84.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.84.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.84.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.84.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.84.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.84.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.84.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.84.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.84.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.83.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.83.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.83.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.83.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.83.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.83.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.83.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.83.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.83.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.82.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.82.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.82.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.82.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.82.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.82.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.82.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.82.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.82.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.81.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.81.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.81.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.81.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.81.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.81.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.81.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.81.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.81.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.80.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.80.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.80.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.78.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.78.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.78.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.78.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.78.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.78.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.76.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.76.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.76.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.75.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.75.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.75.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.75.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.75.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.75.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.74.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.74.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.74.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.74.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.74.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.74.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.73.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.73.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.73.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.73.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.73.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.73.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.72.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.72.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.72.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.72.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.72.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.72.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.71.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.71.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.71.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.70.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.70.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.70.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.70.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.70.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.70.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.70.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.70.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.70.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.69.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.69.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.69.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.68.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.68.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.68.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.68.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.68.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.68.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.68.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.68.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.68.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.67.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.67.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.67.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.67.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.67.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.67.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.66.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.66.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.66.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.66.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.66.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.66.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.65.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.65.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.65.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.64.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.64.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.64.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.64.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.64.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.64.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.64.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.64.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.64.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.63.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.63.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.63.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.62.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.62.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.62.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.62.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.62.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.62.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.61.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.61.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.61.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.61.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.61.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.61.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.60.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.60.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.60.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.59.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.59.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.59.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.58.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.58.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.58.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.57.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.57.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.57.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.56.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.56.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.56.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.56.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.56.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.56.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.55.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.55.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.55.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.55.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.55.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.55.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.54.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.54.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.54.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.54.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.54.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.54.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.54.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.54.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.54.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.53.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.53.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.53.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.52.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.52.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.52.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.52.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.52.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.52.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.51.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.51.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.51.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.51.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.51.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.51.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.50.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.50.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.50.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.50.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.50.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.50.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.49.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.49.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.49.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.48.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.48.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.48.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.47.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.47.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.47.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.46.6](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.6) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.46.6) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.46.5](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.5) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.46.5) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.46.4](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.4) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.46.4) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.46.3](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.3) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.46.3) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.46.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.46.1) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.46.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.46.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.46.0) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.45.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.45.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.45.2) | `MSVC143` `MSVC142` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.45.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.45.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.45.1) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.45.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.45.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.45.0) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.44.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.44.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.44.0) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.43.2](https://github.com/thommyho/gRPC_windows/releases/tag/v1.43.2) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.43.2) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.43.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.43.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.43.0) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.42.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.42.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.42.0) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.41.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.41.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.41.1) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.41.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.41.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.41.0) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.40.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.40.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.40.0) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.39.1](https://github.com/thommyho/gRPC_windows/releases/tag/v1.39.1) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.39.1) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.22.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.22.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.22.0) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.21.4](https://github.com/thommyho/gRPC_windows/releases/tag/v1.21.4) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.21.4) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |
| [1.20.0](https://github.com/thommyho/gRPC_windows/releases/tag/v1.20.0) | [link](https://github.com/thommyho/gRPC_windows_prebuilt/tree/v1.20.0) | `MSVC142` `MSVC141` | :material-check-decagram:{ .tick-blue } | :material-check-decagram:{ .tick-blue } |

The precompiled libraries are attached as assets compressed in zip archives to the bottom of the page.

!!! warning "All releases are built and tested against the compilers listed in the Compiler Set column."

!!! success

    - [x] Downloaded one or more archives e.g.: `MSVC143_64.zip`.
    - [x] Downloaded the corresponding `Examples.zip` of the release.

## Unpack the archives

If you completed the task, proceed as follows to this project setup

```sh
.
├─ vs2015/      # -> From Examples.zip - Directory containing project files (organize source code files and other resources) for Visual Studio 2015
├─ vs2017/      # -> From Examples.zip - Directory containing project files (organize source code files and other resources) for Visual Studio 2017
├─ vs2019/      # -> From Examples.zip - Directory containing project files (organize source code files and other resources) for Visual Studio 2019
├─ vs2022/      # -> From Examples.zip - Directory containing project files (organize source code files and other resources) for Visual Studio 2022
├─ MSVC140_32/  # -> From MSC140_32.zip - Directory containing the prebuilt libraries and header files for Visual Studio 2015 targeting 32-bit
├─ MSVC140_64/  # -> From MSC140_64.zip - Directory containing the prebuilt libraries and header files for Visual Studio 2015 targeting 64-bit
├─ MSVC141_32/  # -> From MSC141_32.zip - Directory containing the prebuilt libraries and header files for Visual Studio 2017 targeting 32-bit
├─ MSVC141_64/  # -> From MSC141_64.zip - Directory containing the prebuilt libraries and header files for Visual Studio 2017 targeting 64-bit
├─ MSVC142_32/  # -> From MSC142_32.zip - Directory containing the prebuilt libraries and header files for Visual Studio 2019 targeting 32-bit
├─ MSVC142_64/  # -> From MSC142_64.zip - Directory containing the prebuilt libraries and header files for Visual Studio 2019 targeting 64-bit
├─ MSVC143_32/  # -> From MSC143_32.zip - Directory containing the prebuilt libraries and header files for Visual Studio 2022 targeting 32-bit
├─ MSVC143_64/  # -> From MSC143_64.zip - Directory containing the prebuilt libraries and header files for Visual Studio 2022 targeting 64-bit
├─ MSVC145_32/  # -> From MSC145_32.zip - Directory containing the prebuilt libraries and header files for Visual Studio 2026 targeting 32-bit
├─ MSVC145_64/  # -> From MSC145_64.zip - Directory containing the prebuilt libraries and header files for Visual Studio 2026 targeting 64-bit

├─ .gitattributes  # Can be ignored.
├─ .gitignore      # Can be ignored.
└─ README.md       # Can be ingored.
```

## Build Examples

### The project setup

Place for holding the Visual Studio Examples source code is following git [repository](https://github.com/thommyho/Cpp-gRPC-Visual-Studio-Examples)

(from version 1.43.0) In every directory there is solution file with `Examples_<vs_compiler_name>.sln` and other directories holding the wanted examples, required project, configuration and resource files. For e.g. vs2019 the directory-file-tree looks like that

```sh
.
├─ vs2019/
│  ├─ 0_HelperScripts/*                      # Contains required helper projects e.g. copying files or calling the protobuf compiler
│  ├─ 1_HelloWorld_Client/*                  # Contains project files and source code for this example
│  ├─ 1_HelloWorld_Server/*                  # ~
│  ├─ 2_HelloWorld_Client_Callback/*         # ~
│  ├─ 2_HelloWorld_Server_Callback/*         # ~
│  ├─ 3_HelloWorld_Client_Async_1/*          # ~
│  ├─ 3_HelloWorld_Client_Async_2/*          # ~
│  ├─ 3_HelloWorld_Server_Async/*            # ~
│  ├─ 4_HelloWorld_Client_Compression/*      # ~
│  ├─ 4_HelloWorld_Server_Compression/*      # ~
│  ├─ 5_HelloWorld_Client_Load_Balancing/*   # ~
│  ├─ 5_HelloWorld_Server_Load_Balancing/*   # ~
│  ├─ 6_HelloWorld_Client_Meta/*             # ~
│  ├─ 6_HelloWorld_Server_Meta/*             # ~
│  ├─ 7_KeyValueStore_Client/*               # ~
│  ├─ 7_KeyValueStore_Server/*               # ~
│  ├─ 8_Route_Guide_Client/*                 # ~
│  ├─ 8_Route_Guide_Server/*                 # ~
│  ├─ 9_Route_Guide_Client_Callback/*        # ~
│  ├─ 9_Route_Guide_Server_Callback/*        # ~
│  ├─ gRPC_PropertySheet/*                   # Contains the property sheet for easy including the required compile and linking dependencies
│  ├─ protos/*                               # Contains the required protofiles of the examples
│  ├─ res/*                                  # Contains required files for specific examples.
│  └─ Examples_vs2019.sln                    # The solution file including and organizing all the example projects
```

### Using Visual Studio IDE :material-microsoft-visual-studio:

!!! warning " Please make sure that you have the correct/any :material-language-cpp: build tools installed. "

Open the `Examples_<vs_compiler_name>.sln` with the required IDE version.
If everything was correctly placed (unpacked), no error popup will appear :stuck_out_tongue_winking_eye:.

!!! help " For further help checkout the FAQ or create an issue. "

And it will look this snapshot using VS 2019 IDE.
![Image title](_assets/images/snapshot_ide_open_vs2019.png)

Click :material-cursor-default-click: `Examples_<vs_compiler_name>` and choose `Build Solution` or simply use the shortcut ++ctrl+shift+b++ to build all examples.

!!! success

    ![Image title](_assets/images/snapshot_ide_success_vs2019.png)

!!! info " Output Directory "

    The output layout follows this scheme

    ```sh
    .
    └─ _out_/
       └─ <architecture>/              # x64 or x86
          └─ <build configuration>/    # Debug, Release or RelWithDebInfo
             └─ <All the examples>/*   # binares and ressources
    ```
