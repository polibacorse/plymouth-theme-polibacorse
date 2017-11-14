%define themename polibacorse
%define set_theme %{_sbindir}/plymouth-set-default-theme
Name:           plymouth-theme-%{themename}
Version:        0.6
Release:        10%{?dist}
Summary:        Plymouth Official Theme for Poliba Corse

Group:          System Environment/Base
License:        CC-BY-SA
URL:            https://github.com/polibacorse
Source0:        https://github.com/polibacorse/%{name}/archive/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       plymouth-plugin-two-step >= 0.7.0
Requires(post): plymouth-scripts

%description
This package represents the official Poliba Corse theme with a progress bar.

%prep
%setup -q

%build
# nada

%install
targetdir=$RPM_BUILD_ROOT/%{_datadir}/plymouth/themes/%{themename}
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $targetdir
install -m 0644 %{themename}.plymouth *.png $targetdir

%post
export LIB=%{_lib}
# on initial install, set this as the new theme
if [ $1 -eq 1 ]; then
    %{set_theme} %{themename}
fi

%postun
export LIB=%{_lib}
# if uninstalling, reset to a boring default theme
if [ $1 -eq 0 ]; then
    if [ "$(%{set_theme})" == "%{themename}" ]; then
        %{set_theme} --reset
    fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%dir %{_datadir}/plymouth/themes/%{themename}
%{_datadir}/plymouth/themes/%{themename}/*.png
%{_datadir}/plymouth/themes/%{themename}/%{themename}.plymouth

%changelog
* Tue Nov 14 2017 Giovanni Grieco <giovanni.grc96@gmail.com> - 0.6
- Forked Hot Dog Plymouth Theme and customised for Poliba Corse.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Will Woods <wwoods@redhat.com> - 0.5-9
- Fix scriptlet errors (#1387308); package no longer rebuilds initramfs.
- Removed all traces of ketchup. NO KETCHUP. EVER.
- Make mustard slightly more vinegar-y

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 03 2011 Will Woods <wwoods@redhat.com> - 0.5-1
- Update README with more links and proper credit for the Hot Dog Creator
- Well more like "The original artist", the Hot Dog is his own Creator
- He is a perfect being who exists beyond Time and Space
- He is a being of pure Delight and Deliciousness
- He transcends the false Beefy/Vegetarian dichotomy
- He tastes really good with mustard
- OBEY THE HOT-DOG, FLOAT WITH HIM INTO ETERNITY
- Various bugfixes

* Sun Oct 02 2011 Will Woods <wwoods@redhat.com> - 0.4-1
- LIVE FROM MILAN IT'S HOT DOG TIME
- Fixed license field
- Updated README
- Rebuild with -funroll-loops
- Hot dog seems much happier

* Tue Mar 15 2011 Will Woods <wwoods@redhat.com> - 0.3-1
- Fix %%post to enable the Beefy Miracle immediately after installation
- Package removal restores bland, meatless default theme
- Package removal does NOT format hard drive or render the user blind/sterile
- Mustard now also indicates victory

* Mon Nov 02 2009 Will Woods <wwoods@redhat.com> - 0.2-1
- Fixed missing progress-01.png

* Fri Oct 30 2009 Will Woods <wwoods@redhat.com> - 0.1-1
- Initial packaging. The mustard indicates progress.
