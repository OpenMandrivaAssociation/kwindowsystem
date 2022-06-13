%define major 5
%define libname %mklibname KF5WindowSystem %{major}
%define devname %mklibname KF5WindowSystem -d
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%global __provides_exclude_from ^(%{_qt5_plugindir}/.*\\.so)$

Name: kwindowsystem
Version:	5.95.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
# Drop win32 support, needed to prevent the dependency generator
# from generating dependencies on Qt5WinExtras
Patch0: kwindowsystem-no-win32.patch
Summary: The KDE Frameworks 5 window system library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-event)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-proto)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xfixes)
# For running version checks
BuildRequires: weston
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}

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
Requires: %{name} = %{EVRD}
Requires: %{name}-backend = %{EVRD}

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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%package x11
Summary: X11 window system plugin for kwindowsystem
Provides: %{name}-backend = %{EVRD}

%description x11
X11 window system plugin for kwindowsystem.

%package wayland
Summary: Wayland window system plugin for kwindowsystem
Provides: %{name}-backend = %{EVRD}

%description wayland
Wayland window system plugin for kwindowsystem.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

L="$(pwd)/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/*.categories
%{_datadir}/qlogging-categories5/kwindowsystem.renamecategories

%files -n %{libname}
%dir %{_libdir}/qt5/plugins/kf5/kwindowsystem
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files x11
%{_libdir}/qt5/plugins/kf5/kwindowsystem/KF5WindowSystemX11Plugin.so

%files wayland

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5WindowSystem
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
