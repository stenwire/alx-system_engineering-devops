# 0x0A-configuration_management

### Configuration management using [Puppet](https://puppet.com/docs/)

<img src="https://vignette2.wikia.nocookie.net/naruto/images/a/a5/Kankur%C5%8D.png/revision/latest?cb=20160108091308">

Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

Install puppet

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](https://puppet.com/docs/)

Install puppet-lint

```
$ gem install puppet-lint
```
