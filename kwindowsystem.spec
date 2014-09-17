%define major 5
%define libname %mklibname KF5WindowSystem %{major}
%define devname %mklibname KF5WindowSystem -d
%define debug_package %{nil}

Name: kwindowsystem
Version: 5.2.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 window system library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xrender)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
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
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5WindowSystem
%{_libdir}/qt5/mkspecs/modules/*
