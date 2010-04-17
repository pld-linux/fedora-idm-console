%define major_version 1.1
%define minor_version 1
Summary:	Fedora Management Console
Name:		fedora-idm-console
Version:	%{major_version}.%{minor_version}
Release:	1
License:	LGPLv2
Group:		Applications/System
Source0:	http://directory.fedoraproject.org/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	4c2b16080a3c6e477924091c02d721bf
URL:		http://directory.fedoraproject.org
BuildRequires:	ant >= 1.6.2
BuildRequires:	idm-console-framework >= 1.1
BuildRequires:	jss >= 4.2
BuildRequires:	ldapsdk
Requires:	idm-console-framework >= 1.1
Requires:	jre-X11
Requires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Java based remote management console used for Managing Fedora
Administration Server and Fedora Directory Server.

%prep
%setup -q

%build
%ant \
	-Dlib.dir=%{_libdir} \
	-Djss.local.location=%{_javadir} \
	-Dbuilt.dir=`pwd`/built

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install built/*.jar $RPM_BUILD_ROOT%{_javadir}
install -d $RPM_BUILD_ROOT%{_bindir}
install built/%{name} $RPM_BUILD_ROOT%{_bindir}

# create symlinks
cd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}_en.jar %{name}-%{major_version}_en.jar
ln -s %{name}-%{version}_en.jar %{name}_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}-%{version}_en.jar
%{_javadir}/%{name}-%{major_version}_en.jar
%{_javadir}/%{name}_en.jar
