Name:      webapp-manager
Version:   {{{ git_dir_version }}}
Release:   1%{?dist}
Summary:   Web Application Manager
License:   GPLv3+
URL:       https://github.com/KyleGospo/webapp-manager
VCS:       {{{ git_dir_vcs }}}
Source:    {{{ git_dir_pack }}}
BuildArch: noarch

Requires: python3-beautifulsoup4
Requires: python3-configobj
Requires: python3-gobject
Requires: python3-pillow
Requires: python3-setproctitle
Requires: python3-tldextract
Requires: xapps

BuildRequires: gettext
BuildRequires: make
BuildRequires: python3-devel

%{?python_disable_dependency_generator}
%global debug_package %{nil}

%description
Launch websites as if they were apps.

%prep
{{{ git_dir_setup_macro }}}
sed -i 's,/usr/lib/,${libdir}/,' usr/bin/%{name}

%build
%make_build
libdir="%{_libdir}" envsubst '$libdir' <usr/bin/%{name} > %{name}
%py_byte_compile %{python3} usr/lib/%{name}/*.py

%install
install -Dm 755 %{name} -t %{buildroot}/%{_bindir}
cp -r etc %{buildroot}/%{_sysconfdir}
cp -r usr/lib %{buildroot}/%{_libdir}
cp -r usr/share %{buildroot}/%{_datadir}
rm -rf %{buildroot}/%{_datadir}/applications/kde4

%files
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/desktop-directories/webapps-webapps.directory
%{_datadir}/glib-2.0/schemas/org.x.%{name}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/categories/applications-webapps.svg
%{_datadir}/locale/
%{_datadir}/%{name}/
%{_sysconfdir}/xdg/menus/applications-merged/webapps.menu

%changelog
{{{ git_dir_changelog }}}
