Summary:	This is OdeiaVir, a program that, well, hates viruses.
Summary(pl):	To OdeiaVir, program, ktory nienawidzi wirusow.
Name:		odeiavir
Version:	0.5.0pre5
Release:	0
License:	GPL
Group:		Applications/Mail
Vendor:		Juan Carlos Castro y Castro <jcastro@vialink.com.br>
Source0:	http://virus.isverybad.org/%{name}-%{version}.tar.gz
#Patch0:		%{name}-what.patch
URL:		http://virus.isverybad.org
#BuildRequires:	-
#PreReq:		-
Requires:	qmail
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is meant to be placed at the local delivery phase of the e-mail
message lifetime. It currently works reliably only with qmail, but
there is embrionary (as in pre-alpha, extremely-untested) Sendmail
support. You call it from the user's .qmail file. This means you can
virus-proof ezmlm lists, too, with ease. Sendmail users will have to
change the Mlocal line in sendmail.cf.

%description -l pl

Kolejny frontend...

%prep
%setup -q -n %{name}-%{version}
#%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8,%{_sysconfdir}/%{name}}

install odeiavir  $RPM_BUILD_ROOT%{_bindir}/odeiavir
install odeiavir.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install config warning.txt $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO scripts *.txt FAQ
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
%{_sysconfdir}/*
