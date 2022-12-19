%bcond_without local_build

Name: telegram-forwarder_auto-Levitsky
Version: 1.0.0
Release: 1%{?dist}
Summary: Telegram forwarder that will automatically forward message
BuildArch: noarch

License: GPLv3+
URL: https://github.com/tim77/telegram-forwarder_auto-Levitsky
%if %{with local_build}
Source0: %{name}.tar.xz
%else
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires: systemd-rpm-macros

Requires: /usr/bin/python
Requires: python3-pip

%description
A telegram forwarder that will automatically forward message from Another
telegram channel(s) / group(s) to Your telegram channel / group.


To enable:
  systemctl --user enable --now telegram-forwarder_auto-Levitsky


%prep
%if %{with local_build}
%autosetup -p1 -n %{name}
%else
%autosetup -p1
%endif


%install
mkdir -p %{buildroot}/opt/%{name}
install -Dpm 0644 %{name}.service -t %{buildroot}%{_userunitdir}
install -Dpm 0644 requirements.txt -t %{buildroot}/opt/%{name}
install -Dpm 0755 %{name}.py -t %{buildroot}/opt/%{name}
install -Dpm 0755 pip-install-and-upgrade.sh -t %{buildroot}/opt/%{name}


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service


%files
/opt/%{name}/
%{_userunitdir}/*.service


%changelog
* Mon Dec 19 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-1
- Initial package
