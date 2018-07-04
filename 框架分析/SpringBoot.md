

# 	Spring Boot

| 作者 | MagnetoWang                                                  |
| ---- | ------------------------------------------------------------ |
| 邮箱 | 暂无                                                         |
| 说明 | 其实把概念弄清楚也就好理解spring boot到底是做什么的。跟着目录走！！！ |
| 注意 | 请不要用于商业用途。分享学习经验是种有趣的爱好。             |
| 参考 | 官方文档和https://github.com/aalansehaiyang/technology-talk/blob/master/basic-knowledge/springboo-note.md |



[TOC]

## To-Do-List

- [ ] [记得图形化这个执行流程](#执行流程)



## 什么是Spring Boot

- 一个框架，用来构建Spring-based 应用。
- 主要开发JAVA应用。



## Spring Boot 支持哪些 [Servlet](# 什么是servlet)

- Tomcat 8.5
- Jetty 9.4
- Undertow 1.4



## [注解讲解](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/bind/annotation/package-summary.html)

| 注解                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| @SpringBootApplication                                       | is equivalent to using @Configuration,@EnableAutoConfiguration, and @ComponentScan with their default attributes |
| @ComponentScan                                               | to find your beans。enable @Component scan on the package where the application is located |
| @EntityScan                                                  | Set the [`packages scanned`](https://docs.spring.io/spring-framework/docs/5.0.7.RELEASE/javadoc-api/org/springframework/orm/jpa/LocalContainerEntityManagerFactoryBean.html?is-external=true#setPackagesToScan-java.lang.String...-) for JPA entities.  Set the packages used with Neo4J's `SessionFactory`.  Set the `initial entity set` used with Spring Data `MongoDB`, `Cassandra` and `Couchbase` mapping contexts. |
| @Configuration                                               | allow to register extra beans in the context or import additional configuration |
| @Import                                                      | 支持导入普通的java类,并将其声明成一个bean                    |
| @[ImportResource](http://www.cnblogs.com/duanxz/p/3787757.html) | 导入资源文件，配合@value 注入值到bean中                      |
| @EnableAutoConfiguration                                     | enable Spring Boot’s auto-configuration mechanism            |
| [@Autowired](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/beans/factory/annotation/Autowired.html) | to do constructor injection                                  |
| [@Controller](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/stereotype/Controller.html) | This annotation serves as a specialization of [`@Component`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/stereotype/Component.html), allowing for implementation classes to be autodetected through classpath scanning. It is typically used in combination with annotated handler methods based on the [`RequestMapping`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/bind/annotation/RequestMapping.html) annotation. 标注一个控制器组件类 |
| [@Service](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/stereotype/Service.html) | May also indicate that a class is a "Business Service Facade" (in the Core J2EE patterns sense), or something similar. This annotation is a general-purpose stereotype and individual teams may narrow their semantics and use as appropriate.  This annotation serves as a specialization of [`@Component`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/stereotype/Component.html), allowing for implementation classes to be autodetected through classpath scanning.  标注一个业务逻辑组件类 |
| [@Repository](https://blog.csdn.net/u010648555/article/details/76299467) | 标注一个DAO组件类 。 an annotated class is a "Repository", originally defined by Domain-Driven Design (Evans, 2003) as "a mechanism for encapsulating storage, retrieval, and search behavior which emulates a collection of objects" |
| [@Component](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/stereotype/Component.html) | 标准一个普通的spring Bean类  Such classes are considered as candidates for auto-detection when using annotation-based configuration and classpath scanning. |
| @Value                                                       | @Value("${property}") to inject configuration properties。is a core container feature, and it does not provide the same features as |
| @ConfigurationProperties.                                    | Relaxed binding，Meta-data support                           |
| @Profile                                                     | to limit when it is loaded                                   |
| @RequestMapping                                              | 提供路由信息                                                 |
| @RestController                                              | 告诉Spring以字符串的形式渲染结果，并直接返回给调用者         |
| @JsonComponent                                               |                                                              |
| @EnableHypermediaSupport                                     |                                                              |
| @Embeddable                                                  |                                                              |
| @JmsListener                                                 |                                                              |
| @KafkaListener                                               |                                                              |
| @Conditional                                                 |                                                              |
| @ConditionalOnClass                                          |                                                              |
| @ConditionalOnMissingBean                                    |                                                              |
| @AutoConfigureAfter                                          |                                                              |
| @AutoConfigureBefore                                         |                                                              |
| @Order                                                       |                                                              |
| @AutoConfigureOrder                                          |                                                              |
| @ConditionalOnProperty                                       |                                                              |
| @ConditionalOnResource                                       |                                                              |
| @Bean                                                        | a method produces a bean to be managed by the Spring container.  主要用于方法上 |
| @PathVaribale                                                | 获取url中的数据                                              |
| @RequestParam                                                | 获取请求参数的值。 handler methods in Servlet and Portlet environments 。  a method parameter should be bound to a web request parameter. |
| @GetMapping                                                  | 组合注解。  is a *composed annotation* that acts as a shortcut for `@RequestMapping(method = RequestMethod.GET)` |
| @PostConstruct                                               | 实现初始化  is a *composed annotation* that acts as a shortcut for `@RequestMapping(method = RequestMethod.POST)` |
| @PreDestroy                                                  | 销毁bean                                                     |
| @Resource                                                    | 标注在字段或属性的setter方法上                               |
| @Qualifier                                                   |                                                              |
| @Scope                                                       |                                                              |
| @RequestMapping                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |
|                                                              |                                                              |

## 注解精讲

### @Autowired

配合着@Component，@Configuration，@ConfigurationProperties用起来会比较方便

功能：主要就是从配置文件读取默认的信息，然后将信息自动配置到已有的java类。也就是javabean。需要@Component来注解，才能配置成功。



### [@Controller](https://blog.csdn.net/u010412719/article/details/69710480)

- 处理http请求
- 必须配合模版来使用 



### @RestController

- 返回json需要@ResponseBody和@Controller配合 
- 是@ResponseBody和@Controller的组合注解 



### [@Component](https://blog.csdn.net/u010648555/article/details/76299467) 



### @RequestParam

- Annotation which indicates that a method parameter should be bound to a web request parameter.

- Supported for annotated handler methods in Servlet and Portlet environments.

- If the method parameter type is `Map` and a request parameter name is specified, then the request parameter value is converted to a `Map` assuming an appropriate conversion strategy is available.

- If the method parameter is `Map<String, String>` or [`MultiValueMap`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/util/MultiValueMap.html) and a parameter name is not specified, then the map parameter is populated with all request parameter names and values.



## 深入理解

### @RestController和@Controller的区别

- 在刚开始学习的时候，做最基础的返回页面html时，@RestController 表示返回的内容都是HTTP Content不会被模版引擎处理的 。所以就是单纯的字符串
- [@Controller 返回才能扫描到资源中html文件](https://blog.csdn.net/baidu_27222643/article/details/78965320)

  



  

  

  

  




## springboot的**加载过程** 



1.如果我们使用的是SpringApplication的静态run方法，首先需要创建一个SpringApplication对象实例。

a）使用SpringFactoriesLoader在应用的classpath中查找并加载所有可用的ApplicationContextInitialize

b）使用SpringFactoriesLoader在应用的classpath中查找并加载所有可用的ApplicationListener

c）设置main方法的定义类

2.开始执行run方法的逻辑，首先遍历执行所有通过SpringFactoriesLoader加载到的SpringApplicationRunListener，调用它们的started()方法，告诉这些SpringApplicationRunListener，SpringBoot应用要开始执行了。

3.创建并配置当前SpringBoot应用将要使用的Environment

4.遍历并调用所有的SpringApplicationRunListener的environmentPrepared()方法，告诉它们，Springboot应用使用的Environment准备好了

5.确定SpringBoot应用创建什么类型的ApplicationContext，并创建完成，然后根据条件决定是否使用自定义的ShutdownHook，是否使用自定义的BeanNameGenerator，是否使用自定义的ResourceLoader，然后将准备好的Environment设置给创建好的ApplicationContext使用

6.ApplicationContext创建完成，SpringApplication调用之前加载的ApplicationContextInitialize的initialize方法对创建好的ApplicationContext进行进一步的处理

7.遍历所有SpringApplicationRunListener的contextPrepared()方法，通知它们，SpringBoot应用使用的ApplicationContext准备好了

8.将之前通过@EnableAutoConfiguration获取的所有配置以及其他形式的Ioc容器配置加载到已经你准备完毕的ApplicationContext

9.遍历所有的SpringApplicationRunListener的contextLoader()方法，告知ApplicationContext已装载完毕

10.调用ApplicationContext的refresh()方法，完成Ioc容器可用的最后一道工序

11.查找当前ApplicationContext中是否注册有CommandLineRunner，如果有，则遍历执行它们

12.遍历所有的SpringApplicationRunListener的finished()方法，告知，“初始化完成”







## Restart vs Reload

The restart technology provided by Spring Boot works by using two classloaders. Classes that do
not change (for example, those from third-party jars) are loaded into a base classloader. Classes
that you are actively developing are loaded into a restart classloader. When the application is
restarted, the restart classloader is thrown away and a new one is created. This approach means
that application restarts are typically much faster than “cold starts”, since the base classloader is
already available and populated.
If you find that restarts are not quick enough for your applications or you encounter classloading
issues, you could consider reloading technologies such as JRebel from ZeroTurnaround. These
work by rewriting classes as they are loaded to make them more amenable to reloading.





## Excluding Resources

Certain resources do not necessarily need to trigger a restart when they are changed. For example,
Thymeleaf templates can be edited in-place. By default, changing resources in /META-INF/maven,
/META-INF/resources, /resources, /static, /public, or /templates does not trigger a
restart but does trigger a live reload. If you want to customize these exclusions, you can use the
spring.devtools.restart.exclude property.



## 配置说明

| 配置文件                            | 文件说明                                                     |
| ----------------------------------- | ------------------------------------------------------------ |
| trigger-file                        | If you work with an IDE that continuously compiles changed files, you might prefer to trigger restarts only |
| Disabling Restart                   | If you do not want to use the restart feature, you can disable it by using the spring.devtools.restart.enabled property. |
| Watching Additional Paths           | You may want your application to be restarted or reloaded when you make changes to files |
| Customizing the Restart Classloader |                                                              |
| Known Limitations                   | Restart functionality does not work well with objects that are deserialized by using a standard ObjectInputStream. |
| LiveReload                          | an embedded LiveReload server that can be used to trigger a browser refresh when a resource is changed |
| Global Settings                     |                                                              |
|                                     |                                                              |
|                                     |                                                              |



## Application Events and Listeners

Some events are actually triggered before the ApplicationContext is created,
so you cannot register a listener on those as a @Bean. You can
register them with the SpringApplication.addListeners(…) method or the
SpringApplicationBuilder.listeners(…) method.
If you want those listeners to be registered automatically, regardless of the way the application is
created, you can add a META-INF/spring.factories file to your project and reference your
listener(s) by using the org.springframework.context.ApplicationListener key, as
shown in the following example:
`org.springframework.context.ApplicationListener=com.example.project.MyListener`



Application events are sent in the following order, as your application runs:

1. An ApplicationStartingEvent is sent at the start of a run but before any processing, except
   for the registration of listeners and initializers.
2. An ApplicationEnvironmentPreparedEvent is sent when the Environment to be used in the
   context is known but before the context is created.
3. An ApplicationPreparedEvent is sent just before the refresh is started but after bean definitions
   have been loaded.
4. An ApplicationStartedEvent is sent after the context has been refreshed but before any
   application and command-line runners have been called.
5. An ApplicationReadyEvent is sent after any application and command-line runners have been
   called. It indicates that the application is ready to service requests.
6. An ApplicationFailedEvent is sent if there is an exception on startup.





## Web Environment

| 概念                                                | 概念说明 |
| --------------------------------------------------- | -------- |
| ApplicationContext                                  |          |
| WebApplicationType                                  |          |
| AnnotationConfigServletWebServerApplicationContext  |          |
| AnnotationConfigReactiveWebServerApplicationContext |          |
| AnnotationConfigApplicationContext                  |          |
| setApplicationContextClass(…).                      |          |
| WebClient                                           |          |
| setWebApplicationType(WebApplicationType).          |          |
|                                                     |          |



## Static Content

By default, Spring Boot serves static content from a directory called /static (or /public or /
resources or /META-INF/resources) in the classpath or from the root of the ServletContext.

It uses the ResourceHttpRequestHandler from Spring MVC so that you can modify that behavior
by adding your own WebMvcConfigurer and overriding the addResourceHandlers method.



## Spring HATEOAS

If you develop a RESTful API that makes use of hypermedia, Spring Boot provides auto-configuration
for Spring HATEOAS that works well with most applications. The auto-configuration replaces the
need to use @EnableHypermediaSupport and registers a number of beans to ease building

hypermedia-based applications, including a LinkDiscoverers (for client side support) and an
ObjectMapper configured to correctly marshal responses into the desired representation. The
ObjectMapper is customized by setting the various spring.jackson.* properties or, if one exists,
by a Jackson2ObjectMapperBuilder bean.
You can take control of Spring HATEOAS’s configuration by using @EnableHypermediaSupport.
Note that doing so disables the ObjectMapper customization described earlier.





## Calling REST Services with RestTemplate

If you need to call remote REST services from your application, you can use the Spring Framework’s
RestTemplate class. Since RestTemplate instances often need to be customized before being
used, Spring Boot does not provide any single auto-configured RestTemplate bean. It does,
however, auto-configure a RestTemplateBuilder, which can be used to create RestTemplate
instances when needed. The auto-configured RestTemplateBuilder ensures that sensible
HttpMessageConverters are applied to RestTemplate instances.

## Calling REST Services with WebClient

If you have Spring WebFlux on your classpath, you can also choose to use WebClient to call remote
REST services. Compared to RestTemplate, this client has a more functional feel and is fully reactive.
You can create your own client instance with the builder, WebClient.create(). See the relevant
section on WebClient.







## 如何启动你的应用

### 说明

在开发中，尤其是在springboot的环境中，尽管我们可以在网上可以找到许多demo代码，但是我们总是无法顺利启动应用或者说执行代码。这里我特别总结一下。启动一个应用到底还需要注意些什么问题。



### 顺利使用@Scheduled这个功能

问题：这里启动应用的时候我遇到了在不同包情况下无法启动应用。因为我把主应用Application.java。放在和我的ScheduledTasks.java文件下同一层次但是不同包名。

操作：应该将Application.java放在ScheduledTasks.java之上。这样可以顺利启动了。





### 顺利使用@ConfigurationProperties这个功能

问题：始终无法读取配置文件中的固定好的常量

操作：要额外加上@PropertySource和@Autowired，路径问题



### 顺利实现文件上传功能

参考链接：https://spring.io/guides/gs/uploading-files/

问题：

- 无法返回html资源，get无法读取文件，post无法读取文件

问题参数：

- [Required request part 'file' is not present](https://www.jianshu.com/p/424017b3ac18) 
- Current request is not a multipart request
- 返回资源问题



操作：

- 绝对是配置问题。最终问题出在bootstrap.yml.  spring:  servlet:    multipart:   改成   spring:  http:    multipart:
- 在postman中删除Headers里面的Content-Type 
- 参考@RestController和@Controller
- get无法读取文件 是因为内部的文件操作，本身就是读取目录的时候有问题。因为已经映射服务器成功了。所以bug好找
- post无法读取文件 主要是配置中的 servlet 和 http 区别。照着例子是过不了的 



































































## 附录

### 什么是Servlet

- 用[Java](https://zh.wikipedia.org/wiki/Java)编写的[服务器](https://zh.wikipedia.org/wiki/%E6%9C%8D%E5%8A%A1%E5%99%A8)端[程序](https://zh.wikipedia.org/wiki/%E7%A8%8B%E5%BA%8F)。其主要功能在于交互式地浏览和修改数据，生成动态[Web](https://zh.wikipedia.org/wiki/Web)内容。 

- 从实现上讲，Servlet可以响应任何类型的请求，但绝大多数情况下Servlet只用来扩展基于[HTTP](https://zh.wikipedia.org/wiki/HTTP)[协议](https://zh.wikipedia.org/wiki/%E5%8D%8F%E8%AE%AE)的[Web服务器](https://zh.wikipedia.org/wiki/Web%E6%9C%8D%E5%8A%A1%E5%99%A8)。 

- javax.servlet.http.HttpServlet实现了专门用于响应[HTTP](https://zh.wikipedia.org/wiki/HTTP)请求的Servlet，提供了响应对应HTTP标准请求的doGet()、doPost()等方法。 

- servlet在服务器的运行生命周期为，在第一次请求（或其实体被内存垃圾回收后再被访问）时被加载并执行一次初始化方法，跟着执行正式运行方法，之后会被常驻并每次被请求时直接执行正式运行方法，直到服务器关闭或被清理时执行一次销毁方法后实体销毁。


### 什么是POJO

- Plain Ordinary Java Object / Pure Old Java Object 
- 翻译成：普通Java类 
- 具有一部分getter/setter方法的,没有业务逻辑的 那种类就可以称作POJO 



### 什么是JavaBean

-  是一种JAVA语言写成的可重用组件 ，类必须是具体的和公共的，并且具有无参数的[构造器](https://baike.baidu.com/item/%E6%9E%84%E9%80%A0%E5%99%A8/9844976) 
- 提供符合一致性设计模式的公共方法将内部域暴露成员属性，set和get方法获取。 
- 一种是有用户界面（UI，User Interface）的JavaBean；还有一种是没有用户界面，主要负责处理事务（如[数据运算](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E8%BF%90%E7%AE%97)，操纵数据库）的JavaBean。JSP通常访问的是后一种JavaBean。 
- 用户可以认为JavaBean提供了一种随时随地的复制和粘贴的功能，而不用关心任何改变。
- 作用：Write once, run anywhere, reuse everywhere  



### 什么是JTA

- IS **Java Transaction API** 
- 统一的事务编程的接口 
- XAResource ：XAResource接口是对实现了X/Open CAE规范的资源管理器 (Resource Manager，数据库就是典型的资源管理器) 的抽象，它由资源适配器 (Resource Apdater) 提供实现。 
- Transaction：Transaction接口是一个事务实例的抽象，通过它可以控制事务内多个资源的提交或者回滚。二阶段提交过程也是由Transaction接口的实现者来完成的。 
- TransactionManager：托管模式 (managed mode) 下，TransactionManager接口是被应用服务器调用，以控制事务的边界的。 
- UserTransaction：非托管模式 (non-managed mode) 下，应用程序可以通过UserTransaction接口控制事务的边界 

### 什么是Bean

- 使用Spring框架所做的就是两件事：开发Bean、配置Bean 
- 根据配置文件来创建Bean实例，并调用Bean实例的方法完成“依赖注入” 
- beans 是根目录  里面 有许多 bean.
- 支持5种作用域： Singleton：单例模式 ， Prototype：原型模式 ，
-  request：对于每次HTTP请求，使用request定义的Bean都将产生一个新的实例，即每次HTTP请求都会产生不同的Bean实例。当然只有在WEB应用中使用Spring时，该作用域才真正有效。 
- session：对于每次HTTPSession，使用session定义的Bean都将产生一个新的实例时，即每次HTTP Session都将产生不同的Bean实例。同HTTP一样，只有在WEB应用才会有效。 
-  global session：每个全局的HTTPSession对应一个Bean实例。仅在portlet Context的时候才有效。 

```xml

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns="http://www.springframework.org/schema/beans"
	xsi:schemaLocation="http://www.springframework.org/schema/beans
	http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">
	<bean id="bean1" class="com.Bean1">
		<constructor-arg value="chenssy"/>
		<constructor-arg value="35-354"/>
	</bean>
	
</beans>
```

### 什么是ApplicationContext 







## 推荐网站

#### http://www.shangyang.me/2017/03/28/spring-framework-sourcecode-analysis-routine-and-environment-init/