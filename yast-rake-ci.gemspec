#--
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
#   This library is free software; you can redistribute it and/or modify
# it only under the terms of version 2.1 of the GNU Lesser General Public
# License as published by the Free Software Foundation.
#
#   This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
#   You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#++

Gem::Specification.new do |spec|
  spec.name	= "yast-rake-ci"
  spec.version = File.read(File.expand_path("../VERSION", __FILE__)).chomp
  spec.summary = "Rake tasks extending the yast-rake functionality"
  spec.license = "LGPL-2.1"

  spec.author	= "Ladislav Slezak"
  spec.email	= "lslezak@suse.cz"
  spec.homepage	= "http://github.org/yast/yast-rake-ci"

  spec.description = <<-EOT
This Rake tasks extend the functionality of yast-rake tasks to easily run
the tests and checks in Jenkins builds.

The reason for a separage gem is are the huge dependencies which require
installing many other gems. And because they are not needed in all cases it
is a good idea to move them to a separate gem.
  EOT

  # gem content
  spec.files   = Dir["lib/tasks/*.rake", "lib/yast/*.rb", "COPYING", "VERSION",
    "Rakefile", ".rubocop.yml"]

  # define LOAD_PATH
  spec.require_path = "lib"

  # dependencies
  spec.add_dependency("rake")
  spec.add_dependency("yast-rake")

  # dependencies needed for the tests
  spec.add_dependency("coveralls")
  spec.add_dependency("gettext")
  spec.add_dependency("raspell")
  # freeze the rubocop version
  spec.add_dependency("rubocop", "0.29.1")
  spec.add_dependency("simplecov")
  spec.add_dependency("yard")
end
