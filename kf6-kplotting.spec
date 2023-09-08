%define libname %mklibname KF6Plotting
%define devname %mklibname KF6Plotting -d
%define git 20230909

Name: kf6-kplotting
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kplotting/-/archive/master/kplotting-master.tar.bz2#/kplotting-%{git}.tar.bz2
Summary: QWidget-derived class that provides a virtual base class for easy data-plotting
URL: https://invent.kde.org/frameworks/kplotting
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
Requires: %{libname} = %{EVRD}

%description
QWidget-derived class that provides a virtual base class for easy data-plotting

%package -n %{libname}
Summary: QWidget-derived class that provides a virtual base class for easy data-plotting
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
QWidget-derived class that provides a virtual base class for easy data-plotting

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

QWidget-derived class that provides a virtual base class for easy data-plotting

%prep
%autosetup -p1 -n kplotting-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files

%files -n %{devname}
%{_includedir}/KF6/KPlotting
%{_libdir}/cmake/KF6Plotting
%{_qtdir}/mkspecs/modules/qt_KPlotting.pri
%{_qtdir}/doc/KF6Plotting.*

%files -n %{libname}
%{_libdir}/libKF6Plotting.so*

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kplotting6widgets.so
