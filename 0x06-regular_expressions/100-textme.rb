#!/usr/bin/env ruby
puts ARGV[0].scan(/\[[a-z]{4}:(.+?)\]\s\[to:(\+?\d+)\]\s\[flags:([-\d:]*)\]/).join(",")
