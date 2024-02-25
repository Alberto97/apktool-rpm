Name:           apktool
Version:        2.9.3
Release:        1%{?dist}
Summary:        A tool for reverse engineering Android apk files

License:        Apache
URL:            https://ibotpeaches.github.io/Apktool/
Source0:        https://raw.githubusercontent.com/iBotPeaches/Apktool/v%{version}/scripts/linux/%{name}
Source1:        https://github.com/iBotPeaches/Apktool/releases/download/v%{version}/%{name}_%{version}.jar

BuildArch:      noarch

Requires:       java

%description
A tool for reverse engineering 3rd party, closed, binary Android apps. It can decode resources to nearly original form and rebuild them after making some modifications. It also makes working with an app easier because of the project like file structure and automation of some repetitive tasks like building apk, etc.


%install
install -d "%{buildroot}%{_bindir}"
install -Dm 0755 %{SOURCE0} "%{buildroot}%{_datadir}/%{name}/%{name}"
install -Dm 0644 %{SOURCE1} "%{buildroot}%{_datadir}/%{name}/%{name}.jar"
%{__ln_s} -f ../share/%{name}/%{name} %{buildroot}%{_bindir}/%{name}


%files
%{_bindir}/%{name}
%{_datadir}/%{name}/*


%changelog
* Sun Feb 25 2024 Alberto Pedron <albertop2197@gmail.com> - 2.9.3-1
- Update to v2.9.3

* Sat Jan 13 2024 Alberto Pedron <albertop2197@gmail.com> - 2.9.2-1
- Update to v2.9.2

* Sat Jan 13 2024 Alberto Pedron <albertop2197@gmail.com> - 2.9.1-1
- Update to v2.9.1

* Sat Oct 28 2023 Alberto Pedron <albertop2197@gmail.com> - 2.9.0-1
- Update to v2.9.0

* Mon Jul 24 2023 Alberto Pedron <albertop2197@gmail.com> - 2.8.1-1
- Update to v2.8.1

* Wed Jul 19 2023 Alberto Pedron <albertop2197@gmail.com> - 2.8.0-1
- Update to v2.8.0

* Sun Nov 27 2022 Alberto Pedron <albertop2197@gmail.com>
- Initial release
