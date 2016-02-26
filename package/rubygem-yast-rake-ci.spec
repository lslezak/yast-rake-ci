#
# spec file for package rubygem-yast-rake-ci
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-yast-rake-ci
Version:        0.0.3
Release:        0
%define mod_name yast-rake-ci
%define mod_full_name %{mod_name}-%{version}
# MANUAL
# extra dependencies (not specified in gemspec)
BuildRequires:  aspell-en
# the rubocop shared config
BuildRequires:  yast2-devtools
# for the tests
BuildRequires:  rubygem(yast-rake)
BuildRequires:  rubygem(rubocop) = 0.29.1
BuildRequires:  rubygem(gettext)
BuildRequires:  rubygem(raspell)
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            http://github.org/yast/yast-rake-ci
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Rake tasks extending the yast-rake functionality
License:        LGPL-2.1
Group:          Development/Languages/Ruby

%description
This Rake tasks extend the functionality of yast-rake tasks to easily run
the tests and checks in Jenkins builds.
The reason for a separage gem is are the huge dependencies which require
installing many other gems. And because they are not needed in all cases it
is a good idea to move them to a separate gem.

%prep

%build

%install
%gem_install \
  --no-rdoc --no-ri \
  -f

# MANUAL
%check
(cd %{buildroot}%{gem_base}/gems/%{mod_full_name} && rake --verbose --trace check:ci)
#/ MANUAL

%gem_packages

%changelog
