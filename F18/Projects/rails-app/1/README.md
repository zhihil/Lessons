# Lesson 1: Intro to Ruby on Rails
Welcome! In the first lesson we'll go through the following:
1. Setup
2. Creating a new rails app
3. Parts of the app
4. Resources

## 1. Setup
First, you'll need your development environment set up. Some things you'll need: 
- Ruby
- Rails
- some IDE / text editor of your choice
- Git
- Git Bash (needed if you have Windows only)
(http://railsinstaller.org/en)

## Creating a new rails app
To create a new rails app, change directory (cd) into your specified folder (in this case it's called workspace), run the rails command, and cd into the newly created app folder:
````
$ cd ~/workspace
$ rails new YOUR_APP_NAME_HERE
$ cd YOUR_APP_NAME_HERE/
````
Rails will generate a bunch of things in creating the app, including a Gemfile. To install all the gems in the Gemfile without production gems, run:
````
$ bundle install --without production
````

## 2. Parts of the app
### Gemfile
This is where the gems are stored. Each gem is a ruby library that extends functionality.
```ruby
source 'https://rubygems.org'

gem 'rails',        '5.1.6'
gem 'puma',         '3.9.1'
gem 'sass-rails',   '5.0.6'
gem 'uglifier',     '3.2.0'
gem 'coffee-rails', '4.2.2'
gem 'jquery-rails', '4.3.1'
gem 'turbolinks',   '5.0.1'
gem 'jbuilder',     '2.7.0'

group :development, :test do
  gem 'sqlite3', '1.3.13'
  gem 'byebug',  '9.0.6', platform: :mri
end

group :development do
  gem 'web-console',           '3.5.1'
  gem 'listen',                '3.1.5'
  gem 'spring',                '2.0.2'
  gem 'spring-watcher-listen', '2.0.1'
end

group :test do
  gem 'rails-controller-testing', '1.0.2'
  gem 'minitest',                 '5.10.3'
  gem 'minitest-reporters',       '1.1.14'
  gem 'guard',                    '2.13.0'
  gem 'guard-minitest',           '2.4.4'
end

group :production do
  gem 'pg', '0.18.4'
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]
```

### app/controllers/application_controller.rb
```ruby
class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception

  def hello
    render html: "hello, world!"
  end
end
```

### config/routes.rb
```ruby
Rails.application.routes.draw do
  root 'application#hello'
end
```

## Resources
### Learn Ruby!
https://www.codecademy.com/learn/learn-ruby
https://www.learnrubyonline.org/en/Hello,_World!

### Learn Git!
https://learngitbranching.js.org/
https://www.codecademy.com/learn/learn-git
