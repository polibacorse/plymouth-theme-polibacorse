Name:		plymouth-theme-polibacorse
Version:	1.0
Release:	1%{?dist}
Summary:	A theme that features the official logo of Poliba Corse with a progress bar underneath.

License:	CC-BY-SA 4.0
URL:		https://github.com/polibacorse
Source0:	https://github.com/polibacorse/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:	noarch
Requires:	plymouth, plymouth-plugin-two-step

%description
The official logo of Poliba Corse as boot splash, ported to Plymouth as a theme.

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT${_datadir}/plymouth/themes/polibacorse
for i in * ; do
	install -p -m 644 $i $RPM_BUILD_ROOT${_datadir}/plymouth/themes/polibacorse
done

plymouth-set-default-theme -R polibacorse

%files
%license LICENSE
${_datadir}/plymouth/themes/polibacorse/

%changelog
* Wed Nov 1 2017 Giovanni Grieco <giovanni.grc96@gmail.com> - 1.0-1
- Package created.

