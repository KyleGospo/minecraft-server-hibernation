Name:           msh-dev
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Autostart and stop minecraft-server when players join/leave 
License:        GPLv3
URL:            https://github.com/KyleGospo/minecraft-server-hibernation

Source:         {{{ git_dir_pack }}}

BuildRequires:  golang
BuildRequires:  git

Conflicts:      msh

%description
Avoid wasting of resources by automatically starting your minecraft server when a player join and stopping it when no one is online

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build
go build .

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 ./msh %{buildroot}/%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/msh

%changelog
{{{ git_dir_changelog }}}