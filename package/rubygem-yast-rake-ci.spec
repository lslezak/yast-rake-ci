#
# spec file for package rubygem-yast-rake-ci
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rubygem-yast-rake-ci
Version:        0.0.1
Release:        0
%define mod_name yast-rake-ci
%define mod_full_name %{mod_name}-%{version}

# extra dependencies (not specified in gemspec)
BuildRequires:  aspell-en
Requires:       aspell-en
# the rubocop shared config
BuildRequires:  yast2-devtools
Requires:       yast2-devtools
# for the tests
BuildRequires:  rubygem(gettext)
BuildRequires:  rubygem(raspell)
BuildRequires:  rubygem(rubocop) = 0.29.1
BuildRequires:  rubygem(yast-rake)

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 3
Url:            http://github.org/yast/yast-rake-ci
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Rake tasks extendind the yast-rake functionality
License:        LGPL-2.1
Group:          Development/Languages/Ruby

%description
This Rake tasks extend the functionality of yast-rake tasks to easily run
the tests and checks in Jenkins builds.
The reason for a separage gem is are the huge dependedncies which require
installing many other gems. And because they are not needed in all cases it
is a good idea to move them to a separate gem.

%package doc
Summary:        RDoc documentation for %{mod_name}
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}

%description doc
Documentation generated at gem installation time.
Usually in RDoc and RI formats.

%prep
#gem_unpack
#if you need patches, apply them here and replace the # with a % sign in the surrounding lines
#gem_build

%build

%install
%gem_install -f

%files
%defattr(-,root,root,-)
%{gem_base}/cache/%{mod_full_name}.gem
%{gem_base}/gems/%{mod_full_name}/
%{gem_base}/specifications/%{mod_full_name}.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{gem_base}/doc

%changelog
