#
%global bastillion_release 3.15_00

Name: bastillion-jetty
Version: 3.15.00
Release: 0.1%{?dist}
License: prosperity3.0

Url: https://github.com/bastillion-io/Bastillion/
BuildArch: noarch

Source: https://github.com/bastillion-io/Bastillion/releases/download/v3.15.00/bastillion-jetty-v%{bastillion_release}.tar.gz

Summary: Bastillion web-based SSH console using Jetty

%description
Bastillion is a web-based SSH console that centrally manages administrative access to systems. Web-based administration is combined with management and distribution of user's public SSH keys. Key management and administration is based on profiles assigned to defined users.

BuildRequires: rsync
# Recent enough freestanding java
Requires: java-headless >= 21

%prep
%setup -n Bastillion-jetty

%build
# No build steps, this is pre-packaged by Bastillion

%install
%{__install} -d -m755  %{buildroot}/opt/%{name}/
rsync -a ./ %{buildroot}/opt/%{name}/
ls -al %{buildroot}/opt/%{name}/

%files
%license LICENSE.md 3rdPartyLicenses.md
%doc README.md
%doc SECURITY.md
/opt/%{name}

%changelog
* Thu Sep 5 2024 Nico Kadel-Garcia
- Initial setup
