# For keeping webpack bundles up-to-date during a testing workflow.
# If you don't keep this process going, you will rebuild the assets per spec run. This is configured
# in rails_helper.rb.

# Build client assets, watching for changes.
rails-client-assets: sh -c 'bundle exec rake react_on_rails:locale && yarn run build:dev:client'

# Build server assets, watching for changes. Remove if not server rendering.
rails-server-assets: sh -c 'yarn run build:dev:server'
