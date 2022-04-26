### Deploy main branch ###
deploy_main:
	git push heroku main
	git push origin main

### Deploy dev branch ###
deploy_dev:
	git push origin dev

### Test collections mycoins ###
test_my_coins:
	newman run https://www.getpostman.com/collections/b25bf2beeafb2415253c -e myCoins.environment.json -d coinScenarios.json -r htmlextra --reporter-htmlextra-export reports/newman/html/test_my_coins.html

### Test collections searchCoinsWithFilter ###
test_search_coins_with_filter:
	newman run https://www.getpostman.com/collections/bee61346a6a4d37fd282 -e myCoins.environment.json -d coinScenarios.json -r htmlextra --reporter-htmlextra-export reports/newman/html/test_search_coins_with_filter.html

### Test collections userMyCoinsLogin ###
test_user_my_coins_login:
	newman run https://www.getpostman.com/collections/c73d28b97ee6ebc9a424 -e myCoins.environment.json -d coinScenarios.json -r htmlextra --reporter-htmlextra-export reports/newman/html/test_user_my_coins_login.html

### Test all collections ###
all_tests: test_my_coins test_search_coins_with_filter test_user_my_coins_login