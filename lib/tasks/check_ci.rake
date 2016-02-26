#--
# Yast rake
#
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
#
# Rake task for running extra checks at the CI server
#

if File.exist?(".rubocop.yml")
  # run rubocop check if .rubocop.yml is present
  require "rubocop/rake_task"
  RuboCop::RakeTask.new
  code_check = :rubocop
else
  # otherwise run a simple syntax check
  code_check = :"check:syntax"
end

dependencies = [:"test:unit", code_check, :"check:pot"]

dependencies << :"check:spelling" if File.exist?(".spell.yml")

# run yardoc if .yardopts is present
if File.exist?(".yardopts")
  require "yard"
  YARD::Rake::YardocTask.new
  dependencies << :yard
end

namespace :check do
  desc "Run CI check tasks (#{dependencies.join(", ")})"
  task ci: dependencies
end

# force running code coverage in the tests
namespace :test do
  task :coverage_setup do
    ENV["COVERAGE"] = "1"
  end

  task test: :coverage_setup
end
