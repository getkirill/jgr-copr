%global commit_hash %(git rev-parse --short HEAD)

Name:           openttd-jgrpp
Version:        0.0.0
Release:        1.%{commit_hash}%{?dist}
Summary:        JGRennison's OpenTTD Patch Pack

License:        GPL-2.0-or-later
URL:            https://github.com/JGRennison/OpenTTD-patches
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  lzo-devel
BuildRequires:  xz-devel
BuildRequires:  libzstd-devel
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel
BuildRequires:  SDL2-devel
BuildRequires:  libicu-devel
BuildRequires:  libcurl-devel

%description
JGRennison's OpenTTD Patch Pack (JGRPP) is a collection of patches and features
for OpenTTD, a transport simulation game based on Transport Tycoon Deluxe.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_exec_prefix}/games/openttd
%{_datadir}/games/openttd
%{_datadir}/applications/openttd.desktop
%{_datadir}/icons/hicolor/*/apps/openttd.png
%{_mandir}/man6/openttd.6*

%changelog
* Wed Feb 05 2025 Your Name <your.email@example.com> - 0.0.0-1
- Initial package of JGRennison's OpenTTD Patch Pack
