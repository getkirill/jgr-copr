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
%global _ttd_bin openttd

%build
%cmake -DCMAKE_INSTALL_BINDIR=bin -DBINARY_NAME=%{_ttd_bin}
%cmake_build

%install
%cmake_install

%files
%license %{_docdir}/%{_ttd_bin}/COPYING.md
%doc %{_docdir}/%{_ttd_bin}
%{_bindir}/%{_ttd_bin}
%{_datadir}/games/%{_ttd_bin}
%{_datadir}/applications/%{_ttd_bin}.desktop
%{_datadir}/icons/hicolor/*/apps/%{_ttd_bin}.png
%{_datadir}/pixmaps/%{_ttd_bin}*
%{_mandir}/man6/%{_ttd_bin}.6*

%changelog
* Wed Feb 05 2025 kraskaska <k.krasilnikov.2008@gmail.com> - 0.0.0-1
- Initial package of JGRennison's OpenTTD Patch Pack
