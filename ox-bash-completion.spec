Name:          ox-bash-completion
BuildArch:     noarch
Version:       1.0.1
Release:       0
Group:         Applications/Productivity
License:       GPL-2.0
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
URL:           http://www.open-xchange.com/
Source:        %{name}_%{version}.tar.xz
Summary:       Bash completion for Open-Xchange commands
Autoreqprov:   no
Requires:      bash
%description
Bash completion for Open-Xchange commands

Authors:
--------
    Carsten Hoeger <choeger@open-xchange.com>

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}/etc/bash_completion.d
install -m 644 ox-bash-completion %{buildroot}/etc/bash_completion.d/ox-bash-completion

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /etc/bash_completion.d
/etc/bash_completion.d/*

%changelog
