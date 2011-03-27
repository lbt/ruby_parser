#
# spec file for package rubygem-ruby_parser (Version 2.0.5)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild
Name:           rubygem-ruby_parser
Version:        2.0.6
Release:        1
%define mod_name ruby_parser
#
Group:          Development/Languages/Ruby
License:        GPLv2+ or Ruby
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
%rubygems_requires
BuildRequires:  rubygem-sexp_processor >= 3.0
Requires:       rubygem-sexp_processor >= 3.0
#
Url:            http://parsetree.rubyforge.org/
Source:         %{mod_name}-%{version}.gem
#
Summary:        ruby_parser (RP) is a ruby parser written in pure ruby (utilizing racc--which does by default use a C extension)
%description
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc--which does by default use a C extension). RP's output is
the same as ParseTree's output: s-expressions using ruby's arrays and
base types.

As an example:

  def conditional1(arg1)
    if arg1 == 0 then
      return 1
    end
    return 0
  end

becomes:

  s(:defn, :conditional1,
   s(:args, :arg1),
   s(:scope,
    s(:block,
     s(:if,
      s(:call, s(:lvar, :arg1), :==, s(:arglist, s(:lit, 0))),
      s(:return, s(:lit, 1)),
      nil),
     s(:return, s(:lit, 0)))))

%prep
%build
%install
%gem_install %{S:0}

# fix require of /usr/local/bin/ruby
sed -i 's,/usr/local/bin/ruby,/usr/bin/ruby,' %{buildroot}%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/test/*.rb

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/ruby_parse
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_name}-%{version}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_name}-%{version}.gemspec
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_name}-%{version}/

%changelog
