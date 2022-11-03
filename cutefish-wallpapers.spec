%define oname wallpapers

Name:           cutefish-wallpapers
Version:        1.0
Release:        1
Summary:        Cutefish Desktop wallpapers
License:        GPL-3.0-or-later
Group:          Unspecified
URL:            https://github.com/cutefishos/wallpapers
Source:         https://github.com/cutefishos/wallpapers/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz
BuildRequires:  cmake
Recommends:     cutefish-filemanager
BuildArch:      noarch

%description
Cutefish Desktop wallpapers.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%cmake

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/cutefishos/
