from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os


class Instagram:

    def __init__(self,driverpath,USER_NAME,PASSWORD):
        self.driver = webdriver.Chrome(executable_path=driverpath)
        self.username = USER_NAME
        self.password = PASSWORD
        self.login()
        

    def login(self):
        '''login into instagram'''
        self.driver.get(url="https://www.instagram.com/")
        time.sleep(3)
        user_name = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
        user_name.send_keys(self.username)
        password = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')))
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        self.notification()


    def notification(self):
        '''cancle save info and notification '''
        time.sleep(4)
        try:
            notification = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')))
            notification.click()
        except NoSuchElementException:
            print("No Notifiction popup found")
        

    def explore_tab(self):
        explorer = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
        explorer.click() 


    def search(self,SEARCH):
        '''search the profile by passing in the name'''
        time.sleep(4)
        self.driver.get(url=f"https://www.instagram.com/{SEARCH}")


    def like_all_post(self,post):
        time.sleep(4)
        try:
            choose_first_pic = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]')
            choose_first_pic.click()
        except NoSuchElementException:
            choose_first_pic = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]')
            choose_first_pic.click()
        time.sleep(4)
        count = 0
        for _ in range(post):
            like = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
            like.click()
            time.sleep(4)
            os.system("cls")
            try:
                next_pic = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]')
            except NoSuchElementException:
                next_pic = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a')
            next_pic.click()
            count +=1
            print(f"{count}/{post}")
            time.sleep(4)
        time.sleep(4)
        cancel = self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/button')
        cancel.click()
            

    def sendmessage(self,MESSAGE):
        time.sleep(4)
        try:
            send_text = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
            send_text.click()
        except NoSuchElementException:
            print("No message button found")
            ask = input("you can send message send follow request insted? Type(y/n): ")
            if ask == "y":
                self.follow()
            else:
                self.driver.quit()
        else:
            time.sleep(4)
            message = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            message.send_keys(MESSAGE)
            message.send_keys(Keys.ENTER)


    def follow(self):
        time.sleep(4)
        '''follow people'''
        follow = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
        # //*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button
        follow.click()

        
    def post_count(self):
        time.sleep(4)
        post = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span').text
        if "," in post:
            post_over_thousands = int(post.replace(",",""))
            return post_over_thousands
        else:
            post_under_thousand = int(post)
            return post_under_thousand


    def followers_count(self):
        '''returns followers count in int'''
        time.sleep(4)
        get_count = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title')
        follower_count = int(get_count.replace(",",""))
        return follower_count

        
    def followers(self):
        '''see the followers'''
        time.sleep(4)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        

    def follow_all_the_followers(self,followers):
        '''follows all the followers of the profile'''
        time.sleep(4)
        for n in range(1,followers+1):
            already_following = self.driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[{n}]/div/div[3]/button').text
            if already_following == "Following":
                pass
            else:
                follow = self.driver.find_element_by_xpath(f'/html/body/div[5]/div/div/div[2]/ul/div/li[{n}]/div/div[3]/button')
                time.sleep(3)
                follow.click()

    # currently not working
    # def scroll_followers_popup(self):
    #     '''will scroll through the followers list'''
    #     time.sleep(4)
    #     scroll = self.driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]')
    #     for _ in range(35):
    #         self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",scroll)
    #         time.sleep(2)



    