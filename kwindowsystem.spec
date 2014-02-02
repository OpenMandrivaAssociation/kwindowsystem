%define major 5
%define libname %mklibname KF5WindowSystem %{major}
%define devname %mklibname KF5WindowSystem -d
%define debug_package %{nil}

Name: kwindowsystem
Version: 4.95.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 window system library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5

%description
KWindowSystem provides access to certain properties and features of the
window manager.

KWindowSystem provides information about the state of the window
manager and allows asking the window manager to change them using a
more high-level interface than the NETWinInfo/NETRootInfo lowlevel
classes.

%package -n %{libname}
Summary: The KDE Frameworks 5 window system library
Group: System/Libraries

%description -n %{libname}
KWindowSystem provides access to certain properties and features of the
window manager.

KWindowSystem provides information about the state of the window
manager and allows asking the window manager to change them using a
more high-level interface than the NETWinInfo/NETRootInfo lowlevel
classes.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
KWindowSystem provides access to certain properties and features of the
window manager.

KWindowSystem provides information about the state of the window
manager and allows asking the window manager to change them using a
more high-level interface than the NETWinInfo/NETRootInfo lowlevel
classes.

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5WindowSystem
