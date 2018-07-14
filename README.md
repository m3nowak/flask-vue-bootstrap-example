# flask-vue-bootstrap-example
Simple example of a project based on those 3 technologies

Frontend tortures in node and vue
Backend fun in python

Node project is contained entirely in "client" folder, however, running "npm run build" will output files to "static" folder at the root of repository.
"npm run dev" configuration requires flask dev server to be running as well. Webpack dev server is actively redirecting any request sent to "/api" to flask dev server.
