LOCAL APK / SDK / AUTH READ-ONLY SCAN
==============================================================================
Root folder: C:\Users\Admin\Desktop\apk-easy-tool-1-60\1-Decompiled APKs\haitacphucsinh-1.1.8
Files visited: 11201
Text bytes inspected: 16212862
Skipped oversized text files: 0
Note: filenames and source references are clues, not proof of server behavior.
Binary DEX/SO/assets are not decompiled by this scanner; use APKTool/JADX separately.
Sensitive-looking values in matching lines are redacted where recognized.

[1] FILE NAMES WORTH OPENING FIRST (highest keyword matches first)
------------------------------------------------------------------------------
[020] smali\com\android\billingclient\api\BillingConfigResponseListener.smali  (matched: response, config)
[020] smali\com\google\android\datatransport\cct\CctTransportBackend$HttpRequest.smali  (matched: http, request)
[020] smali\com\google\android\datatransport\cct\CctTransportBackend$HttpResponse.smali  (matched: http, response)
[020] smali\com\google\android\datatransport\cct\internal\AutoBatchedLogRequestEncoder$NetworkConnectionInfoEncoder.smali  (matched: network, request)
[020] smali\com\google\android\gms\common\api\Api$ApiOptions$HasAccountOptions.smali  (matched: account, api)
[020] smali\com\google\android\gms\common\api\Api$ApiOptions$HasGoogleSignInAccountOptions.smali  (matched: account, api)
[020] smali\com\google\android\gms\common\moduleinstall\internal\ApiFeatureRequest.smali  (matched: api, request)
[020] smali\com\google\android\gms\location\GeofencingRequest$InitialTrigger.smali  (matched: request, init)
[020] smali\com\google\firebase\encoders\proto\AtProtobuf$ProtobufImpl.smali  (matched: protobuf, proto)
[020] smali\com\google\firebase\encoders\proto\AtProtobuf.smali  (matched: protobuf, proto)
[020] smali\com\google\firebase\encoders\proto\Protobuf$IntEncoding.smali  (matched: protobuf, proto)
[020] smali\com\google\firebase\encoders\proto\Protobuf.smali  (matched: protobuf, proto)
[020] smali\com\google\firebase\encoders\proto\ProtobufDataEncoderContext$$ExternalSyntheticLambda0.smali  (matched: protobuf, proto)
[020] smali\com\google\firebase\encoders\proto\ProtobufDataEncoderContext$1.smali  (matched: protobuf, proto)
[020] smali\com\google\firebase\encoders\proto\ProtobufDataEncoderContext.smali  (matched: protobuf, proto)
[020] smali\com\google\firebase\encoders\proto\ProtobufEncoder$Builder$$ExternalSyntheticLambda0.smali  (matched: protobuf, proto)
[020] smali\com\google\firebase\encoders\proto\ProtobufEncoder$Builder.smali  (matched: protobuf, proto)
[020] smali\com\google\firebase\encoders\proto\ProtobufEncoder.smali  (matched: protobuf, proto)
[020] smali\com\google\firebase\encoders\proto\ProtobufValueEncoderContext.smali  (matched: protobuf, proto)
[010] assets\bin\Data\boot.config  (matched: config)
[010] assets\bin\Data\RuntimeInitializeOnLoads.json  (matched: init)
[010] assets\UnityServicesProjectConfiguration.json  (matched: config)
[010] smali\android\support\v4\app\INotificationSideChannel$Stub$Proxy.smali  (matched: channel)
[010] smali\android\support\v4\app\INotificationSideChannel$Stub.smali  (matched: channel)
[010] smali\android\support\v4\app\INotificationSideChannel.smali  (matched: channel)
[010] smali\androidx\activity\ComponentActivity$NonConfigurationInstances.smali  (matched: config)
[010] smali\androidx\activity\result\contract\ActivityResultContracts$RequestMultiplePermissions.smali  (matched: request)
[010] smali\androidx\activity\result\contract\ActivityResultContracts$RequestPermission.smali  (matched: request)
[010] smali\androidx\activity\result\IntentSenderRequest$1.smali  (matched: request)
[010] smali\androidx\activity\result\IntentSenderRequest$Builder.smali  (matched: request)
[010] smali\androidx\activity\result\IntentSenderRequest.smali  (matched: request)
[010] smali\androidx\annotation\ChecksSdkIntAtLeast.smali  (matched: sdk)
[010] smali\androidx\annotation\RequiresApi.smali  (matched: api)
[010] smali\androidx\collection\MapCollections$MapIterator.smali  (matched: api)
[010] smali\androidx\core\app\ActivityCompat$OnRequestPermissionsResultCallback.smali  (matched: request)
[010] smali\androidx\core\app\ActivityCompat$RequestPermissionsRequestCodeValidator.smali  (matched: request)
[010] smali\androidx\core\app\FrameMetricsAggregator$FrameMetricsApi24Impl$1.smali  (matched: api)
[010] smali\androidx\core\app\FrameMetricsAggregator$FrameMetricsApi24Impl.smali  (matched: api)
[010] smali\androidx\core\app\NotificationCompatSideChannelService$NotificationSideChannelStub.smali  (matched: channel)
[010] smali\androidx\core\app\NotificationCompatSideChannelService.smali  (matched: channel)
[010] smali\androidx\core\app\NotificationManagerCompat$SideChannelManager$ListenerRecord.smali  (matched: channel)
[010] smali\androidx\core\app\NotificationManagerCompat$SideChannelManager.smali  (matched: channel)
[010] smali\androidx\core\content\res\ConfigurationHelper.smali  (matched: config)
[010] smali\androidx\core\graphics\drawable\WrappedDrawableApi14.smali  (matched: api)
[010] smali\androidx\core\graphics\drawable\WrappedDrawableApi21.smali  (matched: api)
[010] smali\androidx\core\graphics\TypefaceCompatApi21Impl.smali  (matched: api)
[010] smali\androidx\core\graphics\TypefaceCompatApi24Impl.smali  (matched: api)
[010] smali\androidx\core\graphics\TypefaceCompatApi26Impl.smali  (matched: api)
[010] smali\androidx\core\graphics\TypefaceCompatApi28Impl.smali  (matched: api)
[010] smali\androidx\core\graphics\TypefaceCompatApi29Impl.smali  (matched: api)
[010] smali\androidx\core\hardware\fingerprint\FingerprintManagerCompat$AuthenticationCallback.smali  (matched: auth)
[010] smali\androidx\core\hardware\fingerprint\FingerprintManagerCompat$AuthenticationResult.smali  (matched: auth)
[010] smali\androidx\core\os\ConfigurationCompat.smali  (matched: config)
[010] smali\androidx\core\os\LocaleListPlatformWrapper.smali  (matched: platform)
[010] smali\androidx\core\os\UserManagerCompat.smali  (matched: user)
[010] smali\androidx\core\provider\FontRequest.smali  (matched: request)
[010] smali\androidx\core\provider\FontsContractCompat$FontRequestCallback$FontRequestFailReason.smali  (matched: request)
[010] smali\androidx\core\provider\FontsContractCompat$FontRequestCallback.smali  (matched: request)
[010] smali\androidx\core\view\accessibility\AccessibilityNodeProviderCompat$AccessibilityNodeProviderApi16.smali  (matched: api)
[010] smali\androidx\core\view\accessibility\AccessibilityNodeProviderCompat$AccessibilityNodeProviderApi19.smali  (matched: api)
[010] smali\androidx\core\view\animation\PathInterpolatorApi14.smali  (matched: api)
[010] smali\androidx\core\view\InputDeviceCompat.smali  (matched: device)
[010] smali\androidx\core\view\inputmethod\InputContentInfoCompat$InputContentInfoCompatApi25Impl.smali  (matched: api)
[010] smali\androidx\core\view\ViewConfigurationCompat.smali  (matched: config)
[010] smali\androidx\core\view\ViewPropertyAnimatorCompat$ViewPropertyAnimatorListenerApi14.smali  (matched: api)
[010] smali\androidx\fragment\app\FragmentManagerNonConfig.smali  (matched: config)
[010] smali\androidx\lifecycle\CompositeGeneratedAdaptersObserver.smali  (matched: server)
[010] smali\androidx\lifecycle\FullLifecycleObserver.smali  (matched: server)
[010] smali\androidx\lifecycle\FullLifecycleObserverAdapter$1.smali  (matched: server)
[010] smali\androidx\lifecycle\FullLifecycleObserverAdapter.smali  (matched: server)
[010] smali\androidx\lifecycle\GenericLifecycleObserver.smali  (matched: server)
[010] smali\androidx\lifecycle\LifecycleEventObserver.smali  (matched: server)
[010] smali\androidx\lifecycle\LifecycleObserver.smali  (matched: server)
[010] smali\androidx\lifecycle\LifecycleRegistry$ObserverWithState.smali  (matched: server)
[010] smali\androidx\lifecycle\LiveData$AlwaysActiveObserver.smali  (matched: server)
[010] smali\androidx\lifecycle\LiveData$LifecycleBoundObserver.smali  (matched: server)
[010] smali\androidx\lifecycle\LiveData$ObserverWrapper.smali  (matched: server)
[010] smali\androidx\lifecycle\Observer.smali  (matched: server)
[010] smali\androidx\lifecycle\ReflectiveGenericLifecycleObserver.smali  (matched: server)
[010] smali\androidx\lifecycle\ReportFragment$ActivityInitializationListener.smali  (matched: init)
[010] smali\androidx\lifecycle\SingleGeneratedAdapterObserver.smali  (matched: server)
[010] smali\androidx\loader\app\LoaderManagerImpl$LoaderObserver.smali  (matched: server)
[010] smali\androidx\loader\content\Loader$ForceLoadContentObserver.smali  (matched: server)
[010] smali\androidx\tracing\TraceApi18Impl.smali  (matched: api)
[010] smali\androidx\tracing\TraceApi29Impl.smali  (matched: api)
[010] smali\androidx\viewpager\widget\ViewPager$PagerObserver.smali  (matched: server)
[010] smali\com\android\billingclient\api\AccountIdentifiers.smali  (matched: account)
[010] smali\com\android\billingclient\api\AcknowledgePurchaseResponseListener.smali  (matched: response)
[010] smali\com\android\billingclient\api\BillingClient$BillingResponseCode.smali  (matched: response)
[010] smali\com\android\billingclient\api\BillingConfig.smali  (matched: config)
[010] smali\com\android\billingclient\api\ConsumeResponseListener.smali  (matched: response)
[010] smali\com\android\billingclient\api\GetBillingConfigParams$Builder.smali  (matched: config)
[010] smali\com\android\billingclient\api\GetBillingConfigParams.smali  (matched: config)
[010] smali\com\android\billingclient\api\InAppMessageResponseListener.smali  (matched: response)
[010] smali\com\android\billingclient\api\InAppMessageResult$InAppMessageResponseCode.smali  (matched: response)
[010] smali\com\android\billingclient\api\ProductDetailsResponseListener.smali  (matched: response)
[010] smali\com\android\billingclient\api\PurchaseHistoryResponseListener.smali  (matched: response)
[010] smali\com\android\billingclient\api\PurchasesResponseListener.smali  (matched: response)
[010] smali\com\android\billingclient\api\SkuDetailsResponseListener.smali  (matched: response)
[010] smali\com\android\billingclient\api\UserChoiceBillingListener.smali  (matched: user)
[010] smali\com\android\billingclient\api\UserChoiceDetails$Product.smali  (matched: user)
[010] smali\com\android\billingclient\api\UserChoiceDetails.smali  (matched: user)
[010] smali\com\android\billingclient\BuildConfig.smali  (matched: config)
[010] smali\com\google\android\datatransport\backend\cct\BuildConfig.smali  (matched: config)
[010] smali\com\google\android\datatransport\BuildConfig.smali  (matched: config)
[010] smali\com\google\android\datatransport\cct\internal\AutoBatchedLogRequestEncoder$AndroidClientInfoEncoder.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\AutoBatchedLogRequestEncoder$BatchedLogRequestEncoder.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\AutoBatchedLogRequestEncoder$ClientInfoEncoder.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\AutoBatchedLogRequestEncoder$LogEventEncoder.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\AutoBatchedLogRequestEncoder$LogRequestEncoder.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\AutoBatchedLogRequestEncoder.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\AutoValue_BatchedLogRequest.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\AutoValue_LogRequest$1.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\AutoValue_LogRequest$Builder.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\AutoValue_LogRequest.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\AutoValue_LogResponse.smali  (matched: response)
[010] smali\com\google\android\datatransport\cct\internal\AutoValue_NetworkConnectionInfo$1.smali  (matched: network)
[010] smali\com\google\android\datatransport\cct\internal\AutoValue_NetworkConnectionInfo$Builder.smali  (matched: network)
[010] smali\com\google\android\datatransport\cct\internal\AutoValue_NetworkConnectionInfo.smali  (matched: network)
[010] smali\com\google\android\datatransport\cct\internal\BatchedLogRequest.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\LogRequest$Builder.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\LogRequest.smali  (matched: request)
[010] smali\com\google\android\datatransport\cct\internal\LogResponse.smali  (matched: response)
[010] smali\com\google\android\datatransport\cct\internal\NetworkConnectionInfo$Builder.smali  (matched: network)
[010] smali\com\google\android\datatransport\cct\internal\NetworkConnectionInfo$MobileSubtype.smali  (matched: network)
[010] smali\com\google\android\datatransport\cct\internal\NetworkConnectionInfo$NetworkType.smali  (matched: network)
[010] smali\com\google\android\datatransport\cct\internal\NetworkConnectionInfo.smali  (matched: network)
[010] smali\com\google\android\datatransport\runtime\AutoProtoEncoderDoNotUseEncoder$ClientMetricsEncoder.smali  (matched: proto)
[010] smali\com\google\android\datatransport\runtime\AutoProtoEncoderDoNotUseEncoder$GlobalMetricsEncoder.smali  (matched: proto)
[010] smali\com\google\android\datatransport\runtime\AutoProtoEncoderDoNotUseEncoder$LogEventDroppedEncoder.smali  (matched: proto)
[010] smali\com\google\android\datatransport\runtime\AutoProtoEncoderDoNotUseEncoder$LogSourceMetricsEncoder.smali  (matched: proto)
[010] smali\com\google\android\datatransport\runtime\AutoProtoEncoderDoNotUseEncoder$ProtoEncoderDoNotUseEncoder.smali  (matched: proto)
[010] smali\com\google\android\datatransport\runtime\AutoProtoEncoderDoNotUseEncoder$StorageMetricsEncoder.smali  (matched: proto)
[010] smali\com\google\android\datatransport\runtime\AutoProtoEncoderDoNotUseEncoder$TimeWindowEncoder.smali  (matched: proto)
[010] smali\com\google\android\datatransport\runtime\AutoProtoEncoderDoNotUseEncoder.smali  (matched: proto)
[010] smali\com\google\android\datatransport\runtime\AutoValue_SendRequest$1.smali  (matched: request)
[010] smali\com\google\android\datatransport\runtime\AutoValue_SendRequest$Builder.smali  (matched: request)
[010] smali\com\google\android\datatransport\runtime\AutoValue_SendRequest.smali  (matched: request)
[010] smali\com\google\android\datatransport\runtime\backends\AutoValue_BackendRequest$1.smali  (matched: request)
[010] smali\com\google\android\datatransport\runtime\backends\AutoValue_BackendRequest$Builder.smali  (matched: request)
[010] smali\com\google\android\datatransport\runtime\backends\AutoValue_BackendRequest.smali  (matched: request)
[010] smali\com\google\android\datatransport\runtime\backends\AutoValue_BackendResponse.smali  (matched: response)
[010] smali\com\google\android\datatransport\runtime\backends\BackendRequest$Builder.smali  (matched: request)
[010] smali\com\google\android\datatransport\runtime\backends\BackendRequest.smali  (matched: request)
[010] smali\com\google\android\datatransport\runtime\backends\BackendResponse$Status.smali  (matched: response)
[010] smali\com\google\android\datatransport\runtime\backends\BackendResponse.smali  (matched: response)
[010] smali\com\google\android\datatransport\runtime\BuildConfig.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\dagger\internal\ComponentDefinitionType.smali  (matched: init)
[010] smali\com\google\android\datatransport\runtime\ProtoEncoderDoNotUse.smali  (matched: proto)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\AutoValue_SchedulerConfig.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\AutoValue_SchedulerConfig_ConfigValue$1.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\AutoValue_SchedulerConfig_ConfigValue$Builder.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\AutoValue_SchedulerConfig_ConfigValue.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\SchedulerConfig$Builder.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\SchedulerConfig$ConfigValue$Builder.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\SchedulerConfig$ConfigValue.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\SchedulerConfig$Flag.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\SchedulerConfig.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\WorkInitializer$$ExternalSyntheticLambda0.smali  (matched: init)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\WorkInitializer$$ExternalSyntheticLambda1.smali  (matched: init)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\WorkInitializer.smali  (matched: init)
[010] smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\WorkInitializer_Factory.smali  (matched: init)
[010] smali\com\google\android\datatransport\runtime\scheduling\persistence\AutoValue_EventStoreConfig$1.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\persistence\AutoValue_EventStoreConfig$Builder.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\persistence\AutoValue_EventStoreConfig.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\persistence\EventStoreConfig$Builder.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\persistence\EventStoreConfig.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\persistence\EventStoreModule_StoreConfigFactory$InstanceHolder.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\persistence\EventStoreModule_StoreConfigFactory.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\SchedulingConfigModule.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\scheduling\SchedulingConfigModule_ConfigFactory.smali  (matched: config)
[010] smali\com\google\android\datatransport\runtime\SendRequest$Builder.smali  (matched: request)
[010] smali\com\google\android\datatransport\runtime\SendRequest.smali  (matched: request)
[010] smali\com\google\android\gms\auth\api\signin\GoogleSignInAccount.smali  (matched: account)
[010] smali\com\google\android\gms\common\AccountPicker$AccountChooserOptions$Builder.smali  (matched: account)
[010] smali\com\google\android\gms\common\AccountPicker$AccountChooserOptions.smali  (matched: account)
[010] smali\com\google\android\gms\common\AccountPicker.smali  (matched: account)
[010] smali\com\google\android\gms\common\annotation\KeepForSdk.smali  (matched: sdk)
[010] smali\com\google\android\gms\common\annotation\KeepForSdkWithFieldsAndMethods.smali  (matched: sdk)
[010] smali\com\google\android\gms\common\annotation\KeepForSdkWithMembers.smali  (matched: sdk)
[010] smali\com\google\android\gms\common\annotation\NonNullApi.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$AbstractClientBuilder.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$AnyClient.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$AnyClientKey.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$ApiOptions$HasOptions.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$ApiOptions$NoOptions.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$ApiOptions$NotRequiredOptions.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$ApiOptions$Optional.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$ApiOptions.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$BaseClientBuilder.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$Client.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api$ClientKey.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Api.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\ApiException.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\BatchResultToken.smali  (matched: token)
[010] smali\com\google\android\gms\common\api\DataBufferResponse.smali  (matched: response)
[010] smali\com\google\android\gms\common\api\GoogleApi$Settings$Builder.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\GoogleApi$Settings.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\GoogleApi.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\GoogleApiActivity.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\GoogleApiClient$Builder.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\GoogleApiClient$ConnectionCallbacks.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\GoogleApiClient$OnConnectionFailedListener.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\GoogleApiClient.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\HasApiKey.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\internal\ActivityLifecycleObserver.smali  (matched: server)
[010] smali\com\google\android\gms\common\api\internal\ApiExceptionMapper.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\internal\ApiKey.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\internal\BaseImplementation$ApiMethodImpl.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\internal\GoogleApiManager.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\internal\RegisterListenerMethod.smali  (matched: register)
[010] smali\com\google\android\gms\common\api\internal\TaskApiCall$Builder.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\internal\TaskApiCall.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\internal\UnregisterListenerMethod.smali  (matched: register)
[010] smali\com\google\android\gms\common\api\OptionalModuleApi.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\ResolvableApiException.smali  (matched: api)
[010] smali\com\google\android\gms\common\api\Response.smali  (matched: response)
[010] smali\com\google\android\gms\common\api\UnsupportedApiCallException.smali  (matched: api)
[010] smali\com\google\android\gms\common\data\DataBufferObserver$Observable.smali  (matched: server)
[010] smali\com\google\android\gms\common\data\DataBufferObserver.smali  (matched: server)
[010] smali\com\google\android\gms\common\data\DataBufferObserverSet.smali  (matched: server)
[010] smali\com\google\android\gms\common\GoogleApiAvailability.smali  (matched: api)
[010] smali\com\google\android\gms\common\GoogleApiAvailabilityLight.smali  (matched: api)
[010] smali\com\google\android\gms\common\internal\AccountAccessor.smali  (matched: account)
[010] smali\com\google\android\gms\common\internal\AccountType.smali  (matched: account)
[010] smali\com\google\android\gms\common\internal\ApiExceptionUtil.smali  (matched: api)
[010] smali\com\google\android\gms\common\internal\ConnectionTelemetryConfiguration.smali  (matched: config)
[010] smali\com\google\android\gms\common\internal\GetServiceRequest.smali  (matched: request)
[010] smali\com\google\android\gms\common\internal\IAccountAccessor$Stub.smali  (matched: account)
[010] smali\com\google\android\gms\common\internal\IAccountAccessor.smali  (matched: account)
[010] smali\com\google\android\gms\common\internal\ICancelToken$Stub.smali  (matched: token)
[010] smali\com\google\android\gms\common\internal\ICancelToken.smali  (matched: token)
[010] smali\com\google\android\gms\common\internal\RootTelemetryConfigManager.smali  (matched: config)
[010] smali\com\google\android\gms\common\internal\RootTelemetryConfiguration.smali  (matched: config)
[010] smali\com\google\android\gms\common\moduleinstall\ModuleAvailabilityResponse$AvailabilityStatus.smali  (matched: response)
[010] smali\com\google\android\gms\common\moduleinstall\ModuleAvailabilityResponse.smali  (matched: response)
[010] smali\com\google\android\gms\common\moduleinstall\ModuleInstallIntentResponse.smali  (matched: response)
[010] smali\com\google\android\gms\common\moduleinstall\ModuleInstallRequest$Builder.smali  (matched: request)
[010] smali\com\google\android\gms\common\moduleinstall\ModuleInstallRequest.smali  (matched: request)
[010] smali\com\google\android\gms\common\moduleinstall\ModuleInstallResponse.smali  (matched: response)
[010] smali\com\google\android\gms\common\server\response\FastJsonResponse$Field.smali  (matched: response)
[010] smali\com\google\android\gms\common\server\response\FastJsonResponse$FieldConverter.smali  (matched: response)
[010] smali\com\google\android\gms\common\server\response\FastJsonResponse.smali  (matched: response)
[010] smali\com\google\android\gms\common\server\response\FastSafeParcelableJsonResponse.smali  (matched: response)
[010] smali\com\google\android\gms\common\server\response\SafeParcelResponse.smali  (matched: response)
[010] smali\com\google\android\gms\common\UserRecoverableException.smali  (matched: user)
[010] smali\com\google\android\gms\common\util\DeviceProperties.smali  (matched: device)
[010] smali\com\google\android\gms\common\util\DynamiteApi.smali  (matched: api)
[010] smali\com\google\android\gms\common\util\HttpUtils.smali  (matched: http)
[010] smali\com\google\android\gms\common\util\PlatformVersion.smali  (matched: platform)
[010] smali\com\google\android\gms\location\ActivityRecognitionApi.smali  (matched: api)
[010] smali\com\google\android\gms\location\ActivityTransitionRequest.smali  (matched: request)
[010] smali\com\google\android\gms\location\FusedLocationProviderApi.smali  (matched: api)
[010] smali\com\google\android\gms\location\GeofencingApi.smali  (matched: api)
[010] smali\com\google\android\gms\location\GeofencingRequest$Builder.smali  (matched: request)
[010] smali\com\google\android\gms\location\GeofencingRequest.smali  (matched: request)
[010] smali\com\google\android\gms\location\LocationRequest.smali  (matched: request)
[010] smali\com\google\android\gms\location\LocationSettingsRequest$Builder.smali  (matched: request)
[010] smali\com\google\android\gms\location\LocationSettingsRequest.smali  (matched: request)
[010] smali\com\google\android\gms\location\LocationSettingsResponse.smali  (matched: response)
[010] smali\com\google\android\gms\location\SettingsApi.smali  (matched: api)
[010] smali\com\google\android\gms\location\SleepSegmentRequest.smali  (matched: request)
[010] smali\com\google\android\gms\tasks\CancellationToken.smali  (matched: token)
[010] smali\com\google\android\gms\tasks\CancellationTokenSource.smali  (matched: token)
[010] smali\com\google\android\gms\tasks\OnTokenCanceledListener.smali  (matched: token)
[010] smali\com\google\firebase\encoders\config\Configurator.smali  (matched: config)
[010] smali\com\google\firebase\encoders\config\EncoderConfig.smali  (matched: config)
[010] smali\com\google\firebase\encoders\json\BuildConfig.smali  (matched: config)
[010] smali\com\google\firebase\encoders\proto\ProtoEnum.smali  (matched: proto)
[010] smali\com\google\firebase\FirebaseApiNotAvailableException.smali  (matched: api)
[010] smali\com\gosu\sdk\unity\SdkBridge.smali  (matched: sdk)
[010] smali\com\haitac\phucsinh\BuildConfig.smali  (matched: config)
[010] smali\com\unity3d\player\BuildConfig.smali  (matched: config)
[010] smali\com\unity3d\player\GoogleARCoreApi.smali  (matched: api)
[010] smali\com\unity3d\player\IPermissionRequestCallbacks.smali  (matched: request)
[010] smali\com\unity3d\player\NetworkConnectivity.smali  (matched: network)
[010] smali\com\unity3d\player\NetworkConnectivityNougat.smali  (matched: network)
[010] smali\com\unity3d\player\PlatformSupport.smali  (matched: platform)
[010] smali\com\unity3d\player\UnityPermissions$ModalWaitForPermissionResponse.smali  (matched: response)
[010] smali\com\unity\purchasing\BuildConfig.smali  (matched: config)
[010] smali\com\unity\purchasing\common\InitializationFailureReason.smali  (matched: init)
[010] smali\com\unity\purchasing\common\ProductDefinition.smali  (matched: init)
[010] smali\org\fmod\FMODAudioDevice.smali  (matched: device)
[010] unknown\firebase-encoders-proto.properties  (matched: proto)
[010] unknown\transport-api.properties  (matched: api)

[2] SOURCE / CONFIG CONTENT MATCHES
------------------------------------------------------------------------------

FILE: AndroidManifest.xml
    L1 [API route or URL] <?xml version="1.0" encoding="utf-8" standalone="no"?><manifest xmlns:android="http://schemas.android.com/apk/res/android" android:compileSdkVersion="34" android:compileSdkVersionCodename="14" android:installLocation="preferExternal" package="com.haitac.phucsi...

FILE: assets\bin\Data\RuntimeInitializeOnLoads.json
    L1 [SDK/auth keyword] {"root":[{"assemblyName":"Assembly-CSharp","nameSpace":"","className":"SdkRiengEditorLogin","methodName":"ChooseLoginOutsideAndroid","loadTypes":1,"isUnityClass":false},{"assemblyName":"Assembly-CSharp","nameSpace":"","className":"ServerOverride","methodName":...

FILE: assets\bin\Data\ScriptingAssemblies.json
    L1 [HTTP/API client] {"names":["UnityEngine.dll","UnityEngine.AIModule.dll","UnityEngine.ARModule.dll","UnityEngine.AccessibilityModule.dll","UnityEngine.AndroidJNIModule.dll","UnityEngine.AnimationModule.dll","UnityEngine.AssetBundleModule.dll","UnityEngine.AudioModule.dll","Unit...

FILE: assets\UnityServicesProjectConfiguration.json
    L1 [server/config field] {"Keys":["com.unity.services.core.environment-name","com.unity.services.core.version","com.unity.services.core.initializer-assembly-qualified-names","com.unity.purchasing.version","com.unity.purchasing.initializer-assembly-qualified-names","com.unity.services....

FILE: res\color\common_google_signin_btn_text_dark.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\color\common_google_signin_btn_text_light.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\color\common_google_signin_btn_tint.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_icon_dark.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_icon_dark_focused.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_icon_dark_normal.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_icon_disabled.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_icon_light.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_icon_light_focused.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_icon_light_normal.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_text_dark.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_text_dark_focused.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_text_dark_normal.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_text_disabled.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_text_light.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_text_light_focused.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\common_google_signin_btn_text_light_normal.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\notification_action_background.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">
    L6 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\notification_bg.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\notification_bg_low.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\notification_icon_background.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\drawable\notification_tile_bg.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android" />

FILE: res\layout\custom_dialog.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\layout\notification_action.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\layout\notification_action_tombstone.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\layout\notification_template_custom_big.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\layout\notification_template_icon_group.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\layout\notification_template_part_chronometer.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android" />

FILE: res\layout\notification_template_part_time.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android" />

FILE: res\mipmap-anydpi-v26\app_icon.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\mipmap-anydpi-v26\app_icon_round.xml
    L3 [API route or URL] xmlns:android="http://schemas.android.com/apk/res/android">

FILE: res\values-fi\strings.xml
    L9 [identity/device field] <string name="common_google_play_services_notification_channel_name">Google Play Palveluiden saatavuus</string>
    L11 [identity/device field] <string name="common_google_play_services_unknown_issue">Sovelluksella %1$s on ongelmia Google Play Palveluiden kanssa. Yritä uudelleen.</string>
    L17 [identity/device field] <string name="common_google_play_services_wear_update_text">Uusi Google Play Palveluiden versio tarvitaan. Se päivittyy pian.</string>

FILE: res\values-in\strings.xml
    L19 [SDK/auth keyword] <string name="common_signin_button_text">Login</string>
    L20 [SDK/auth keyword] <string name="common_signin_button_text_long">Login dengan Google</string>

FILE: res\values-pt-rBR\strings.xml
    L19 [SDK/auth keyword] <string name="common_signin_button_text">Fazer login</string>
    L20 [SDK/auth keyword] <string name="common_signin_button_text_long">Fazer login com o Google</string>

FILE: smali\androidx\activity\ComponentActivity.smali
    L747 [SDK/auth keyword] invoke-virtual {p2, v0, p0, p1, p3}, Landroidx/activity/result/ActivityResultRegistry;->register(Ljava/lang/String;Landroidx/lifecycle/LifecycleOwner;Landroidx/activity/result/contract/ActivityResultContract;Landroidx/activity/result/ActivityResultCallback;)La...

FILE: smali\androidx\activity\result\ActivityResultRegistry$1.smali
    L11 [SDK/auth keyword] value = Landroidx/activity/result/ActivityResultRegistry;->register(Ljava/lang/String;Landroidx/lifecycle/LifecycleOwner;Landroidx/activity/result/contract/ActivityResultContract;Landroidx/activity/result/ActivityResultCallback;)Landroidx/activity/result/Activ...

FILE: smali\androidx\activity\result\ActivityResultRegistry$2.smali
    L8 [SDK/auth keyword] value = Landroidx/activity/result/ActivityResultRegistry;->register(Ljava/lang/String;Landroidx/lifecycle/LifecycleOwner;Landroidx/activity/result/contract/ActivityResultContract;Landroidx/activity/result/ActivityResultCallback;)Landroidx/activity/result/Activ...

FILE: smali\androidx\activity\result\ActivityResultRegistry$3.smali
    L8 [SDK/auth keyword] value = Landroidx/activity/result/ActivityResultRegistry;->register(Ljava/lang/String;Landroidx/activity/result/contract/ActivityResultContract;Landroidx/activity/result/ActivityResultCallback;)Landroidx/activity/result/ActivityResultLauncher;

FILE: smali\androidx\activity\result\ActivityResultRegistry.smali
    L640 [SDK/auth keyword] .method public final register(Ljava/lang/String;Landroidx/activity/result/contract/ActivityResultContract;Landroidx/activity/result/ActivityResultCallback;)Landroidx/activity/result/ActivityResultLauncher;
    L740 [SDK/auth keyword] .method public final register(Ljava/lang/String;Landroidx/lifecycle/LifecycleOwner;Landroidx/activity/result/contract/ActivityResultContract;Landroidx/activity/result/ActivityResultCallback;)Landroidx/activity/result/ActivityResultLauncher;
    L832 [SDK/auth keyword] const-string p2, " is attempting to register while current state is "
    L843 [SDK/auth keyword] const-string p2, ". LifecycleOwners must call register before they are STARTED."

FILE: smali\androidx\core\app\ActivityCompat$1.smali
    L66 [server/config field] invoke-virtual {v2}, Landroid/app/Activity;->getPackageName()Ljava/lang/String;

FILE: smali\androidx\core\app\ActivityRecreator$1.smali
    L23 [SDK/auth keyword] .field final synthetic val$token:<redacted>;
    L33 [SDK/auth keyword] iput-object p2, p0, Landroidx/core/app/ActivityRecreator$1;->val$token:<redacted>;
    L48 [SDK/auth keyword] iget-object v1, p0, Landroidx/core/app/ActivityRecreator$1;->val$token:<redacted>;

FILE: smali\androidx\core\app\ActivityRecreator$3.smali
    L23 [SDK/auth keyword] .field final synthetic val$token:<redacted>;
    L33 [SDK/auth keyword] iput-object p2, p0, Landroidx/core/app/ActivityRecreator$3;->val$token:<redacted>;
    L66 [SDK/auth keyword] iget-object v6, p0, Landroidx/core/app/ActivityRecreator$3;->val$token:<redacted>;
    L94 [SDK/auth keyword] iget-object v5, p0, Landroidx/core/app/ActivityRecreator$3;->val$token:<redacted>;

FILE: smali\androidx\core\app\NavUtils.smali
    L131 [server/config field] invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;
    L353 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\androidx\core\app\NotificationCompat$DecoratedCustomViewStyle.smali
    L153 [server/config field] invoke-virtual {v2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\androidx\core\app\NotificationCompat$Style.smali
    L349 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\androidx\core\app\NotificationCompatSideChannelService$NotificationSideChannelStub.smali
    L46 [identity/device field] invoke-static {}, Landroidx/core/app/NotificationCompatSideChannelService$NotificationSideChannelStub;->getCallingUid()I
    L85 [identity/device field] invoke-static {}, Landroidx/core/app/NotificationCompatSideChannelService$NotificationSideChannelStub;->getCallingUid()I
    L129 [identity/device field] invoke-static {}, Landroidx/core/app/NotificationCompatSideChannelService$NotificationSideChannelStub;->getCallingUid()I

FILE: smali\androidx\core\app\NotificationCompatSideChannelService.smali
    L40 [identity/device field] invoke-virtual {v0, p1}, Landroid/content/pm/PackageManager;->getPackagesForUid(I)[Ljava/lang/String;
    L73 [identity/device field] const-string v2, "NotificationSideChannelService: Uid "

FILE: smali\androidx\core\app\NotificationManagerCompat$CancelTask.smali
    L25 [server/config field] .field final packageName:Ljava/lang/String;
    L38 [server/config field] iput-object p1, p0, Landroidx/core/app/NotificationManagerCompat$CancelTask;->packageName:Ljava/lang/String;
    L65 [server/config field] iput-object p1, p0, Landroidx/core/app/NotificationManagerCompat$CancelTask;->packageName:Ljava/lang/String;
    L97 [server/config field] iget-object v0, p0, Landroidx/core/app/NotificationManagerCompat$CancelTask;->packageName:Ljava/lang/String;
    L105 [server/config field] iget-object v0, p0, Landroidx/core/app/NotificationManagerCompat$CancelTask;->packageName:Ljava/lang/String;
    L123 [server/config field] const-string v1, "CancelTask[packageName:"
    L128 [server/config field] iget-object v1, p0, Landroidx/core/app/NotificationManagerCompat$CancelTask;->packageName:Ljava/lang/String;

FILE: smali\androidx\core\app\NotificationManagerCompat$NotifyTask.smali
    L25 [server/config field] .field final packageName:Ljava/lang/String;
    L38 [server/config field] iput-object p1, p0, Landroidx/core/app/NotificationManagerCompat$NotifyTask;->packageName:Ljava/lang/String;
    L63 [server/config field] iget-object v0, p0, Landroidx/core/app/NotificationManagerCompat$NotifyTask;->packageName:Ljava/lang/String;
    L82 [server/config field] const-string v1, "NotifyTask[packageName:"
    L87 [server/config field] iget-object v1, p0, Landroidx/core/app/NotificationManagerCompat$NotifyTask;->packageName:Ljava/lang/String;

FILE: smali\androidx\core\app\NotificationManagerCompat$SideChannelManager.smali
    L768 [server/config field] iget-object v5, v5, Landroid/content/pm/ServiceInfo;->packageName:Ljava/lang/String;
    L784 [server/config field] iget-object v6, v6, Landroid/content/pm/ServiceInfo;->packageName:Ljava/lang/String;

FILE: smali\androidx\core\app\NotificationManagerCompat.smali
    L215 [server/config field] invoke-virtual {v5}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;
    L378 [server/config field] invoke-virtual {v2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L383 [identity/device field] iget v1, v1, Landroid/content/pm/ApplicationInfo;->uid:I
    L871 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\androidx\core\app\ShareCompat$IntentBuilder.smali
    L97 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L106 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\androidx\core\content\ContextCompat$LegacyServiceMapHolder.smali
    L99 [SDK/auth keyword] const-class v1, Landroid/media/session/MediaSessionManager;

FILE: smali\androidx\core\content\ContextCompat.smali
    L56 [identity/device field] invoke-static {}, Landroid/os/Process;->myUid()I

FILE: smali\androidx\core\content\PermissionChecker.smali
    L47 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L63 [identity/device field] invoke-static {}, Landroid/os/Binder;->getCallingUid()I
    L100 [identity/device field] invoke-static {}, Landroid/os/Binder;->getCallingUid()I
    L146 [identity/device field] invoke-virtual {p4, p3}, Landroid/content/pm/PackageManager;->getPackagesForUid(I)[Ljava/lang/String;
    L195 [identity/device field] invoke-static {}, Landroid/os/Process;->myUid()I
    L199 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\androidx\core\content\res\TypedArrayUtils.smali
    L7 [API route or URL] .field private static final NAMESPACE:Ljava/lang/String; = "http://schemas.android.com/apk/res/android"
    L484 [API route or URL] const-string v0, "http://schemas.android.com/apk/res/android"

FILE: smali\androidx\core\graphics\drawable\IconCompat.smali
    L798 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L1540 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\androidx\core\graphics\TypefaceCompat.smali
    L270 [identity/device field] invoke-static {p2, p3, p4}, Landroidx/core/graphics/TypefaceCompat;->createResourceUid(Landroid/content/res/Resources;II)Ljava/lang/String;
    L303 [identity/device field] invoke-static {p1, p2, p4}, Landroidx/core/graphics/TypefaceCompat;->createResourceUid(Landroid/content/res/Resources;II)Ljava/lang/String;
    L316 [identity/device field] .method private static createResourceUid(Landroid/content/res/Resources;II)Ljava/lang/String;
    L324 [server/config field] invoke-virtual {p0, p1}, Landroid/content/res/Resources;->getResourcePackageName(I)Ljava/lang/String;
    L353 [identity/device field] invoke-static {p0, p1, p2}, Landroidx/core/graphics/TypefaceCompat;->createResourceUid(Landroid/content/res/Resources;II)Ljava/lang/String;

FILE: smali\androidx\core\provider\FontsContractCompat.smali
    L950 [server/config field] iget-object v3, v2, Landroid/content/pm/ProviderInfo;->packageName:Ljava/lang/String;
    L963 [server/config field] iget-object v0, v2, Landroid/content/pm/ProviderInfo;->packageName:Ljava/lang/String;

FILE: smali\androidx\core\text\util\FindAddress.smali
    L718 [server/config field] const-string v0, "(?:alley|annex|arcade|ave[.]?|avenue|alameda|bayou|beach|bend|bluffs?|bottom|boulevard|branch|bridge|brooks?|burgs?|bypass|broadway|camino|camp|canyon|cape|causeway|centers?|circles?|cliffs?|club|common|corners?|course|courts?|coves?|creek|cr...

FILE: smali\androidx\core\text\util\LinkifyCompat.smali
    L292 [API route or URL] const-string v2, "https://"
    L296 [API route or URL] const-string v5, "http://"

FILE: smali\androidx\core\util\PatternsCompat.smali
    L23 [identity/device field] .field static final IANA_TOP_LEVEL_DOMAINS:Ljava/lang/String; = "(?:(?:aaa|aarp|abb|abbott|abogado|academy|accenture|accountant|accountants|aco|active|actor|ads|adult|aeg|aero|afl|agency|aig|airforce|airtel|allfinanz|alsace|amica|amsterdam|android|apartments|a...
    L43 [identity/device field] .field private static final STRICT_HOST_NAME:Ljava/lang/String; = "(?:(?:[a-zA-Z0-9[\u00a0-\ud7ff\uf900-\ufdcf\ufdf0-\uffef\ud800\udc00-\ud83f\udffd\ud840\udc00-\ud87f\udffd\ud880\udc00-\ud8bf\udffd\ud8c0\udc00-\ud8ff\udffd\ud900\udc00-\ud93f\udffd\ud940\udc00...
    L45 [identity/device field] .field private static final STRICT_TLD:Ljava/lang/String; = "(?:(?:(?:aaa|aarp|abb|abbott|abogado|academy|accenture|accountant|accountants|aco|active|actor|ads|adult|aeg|aero|afl|agency|aig|airforce|airtel|allfinanz|alsace|amica|amsterdam|android|apartments|ap...
    L127 [identity/device field] const-string v3, "(?:(?:(?:[a-zA-Z0-9[\u00a0-\ud7ff\uf900-\ufdcf\ufdf0-\uffef\ud800\udc00-\ud83f\udffd\ud840\udc00-\ud87f\udffd\ud880\udc00-\ud8bf\udffd\ud8c0\udc00-\ud8ff\udffd\ud900\udc00-\ud93f\udffd\ud940\udc00-\ud97f\udffd\ud980\udc00-\ud9bf\udffd\ud9c0\u...

FILE: smali\androidx\core\view\accessibility\AccessibilityNodeInfoCompat.smali
    L1840 [server/config field] .method public getPackageName()Ljava/lang/CharSequence;
    L1846 [server/config field] invoke-virtual {v0}, Landroid/view/accessibility/AccessibilityNodeInfo;->getPackageName()Ljava/lang/CharSequence;
    L3248 [server/config field] .method public setPackageName(Ljava/lang/CharSequence;)V
    L3254 [server/config field] invoke-virtual {v0, p1}, Landroid/view/accessibility/AccessibilityNodeInfo;->setPackageName(Ljava/lang/CharSequence;)V
    L3696 [server/config field] const-string v1, "; packageName: "
    L3701 [server/config field] invoke-virtual {p0}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->getPackageName()Ljava/lang/CharSequence;

FILE: smali\androidx\core\widget\TextViewCompat$OreoCallback.smali
    L112 [server/config field] iget-object v0, v0, Landroid/content/pm/ActivityInfo;->packageName:Ljava/lang/String;
    L236 [server/config field] invoke-virtual {p2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L242 [server/config field] iget-object v1, v1, Landroid/content/pm/ActivityInfo;->packageName:Ljava/lang/String;

FILE: smali\androidx\customview\widget\ExploreByTouchHelper.smali
    L395 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L399 [server/config field] invoke-virtual {p2, p1}, Landroid/view/accessibility/AccessibilityEvent;->setPackageName(Ljava/lang/CharSequence;)V
    L520 [server/config field] invoke-virtual {v3}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L524 [server/config field] invoke-virtual {v0, v3}, Landroidx/core/view/accessibility/AccessibilityNodeInfoCompat;->setPackageName(Ljava/lang/CharSequence;)V

FILE: smali\androidx\fragment\app\Fragment.smali
    L180 [identity/device field] invoke-static {}, Ljava/util/UUID;->randomUUID()Ljava/util/UUID;
    L184 [identity/device field] invoke-virtual {v0}, Ljava/util/UUID;->toString()Ljava/lang/String;
    L1870 [identity/device field] invoke-static {}, Ljava/util/UUID;->randomUUID()Ljava/util/UUID;
    L1874 [identity/device field] invoke-virtual {v0}, Ljava/util/UUID;->toString()Ljava/lang/String;

FILE: smali\androidx\loader\content\Loader.smali
    L657 [SDK/auth keyword] const-string v0, "No listener register"
    L702 [SDK/auth keyword] const-string v0, "No listener register"

FILE: smali\com\android\billingclient\api\AcknowledgePurchaseParams$Builder.smali
    L63 [SDK/auth keyword] const-string v1, "Purchase token must be set"

FILE: smali\com\android\billingclient\api\AlternativeChoiceDetails$Product.smali
    L225 [SDK/auth keyword] const-string v0, "{id: %s, type: %s, offer token: <redacted>}"

FILE: smali\com\android\billingclient\api\BillingClientImpl.smali
    L215 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L240 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L373 [server/config field] invoke-virtual {p3}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L428 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L454 [server/config field] invoke-virtual {p5}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L533 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L559 [server/config field] invoke-virtual {p5}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L827 [server/config field] iget-object v6, v6, Landroid/content/pm/ServiceInfo;->packageName:Ljava/lang/String;
    L1148 [server/config field] invoke-virtual {v10}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L1172 [server/config field] invoke-virtual {v9}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L1313 [SDK/auth keyword] const-string v6, "BUG: empty/null token!"
    L1396 [SDK/auth keyword] const-string v5, "Continuation token: <redacted>
    L2123 [server/config field] invoke-virtual {v10}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L2261 [SDK/auth keyword] const-string v7, "BUG: empty/null token!"
    L2340 [SDK/auth keyword] const-string v6, "Continuation token: <redacted>
    L2526 [SDK/auth keyword] const-string v0, "Please provide a valid purchase token."
    L5196 [server/config field] const-string v0, "skuPackageName"
    L6609 [server/config field] iget-object v7, v7, Landroid/content/pm/ServiceInfo;->packageName:Ljava/lang/String;
    L7153 [server/config field] invoke-virtual {p4}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L7190 [server/config field] invoke-virtual {v2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L7226 [server/config field] invoke-virtual {v3}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L7319 [SDK/auth keyword] const-string v1, "Error consuming purchase with token. Response code: "
    L7321 [SDK/auth keyword] const-string v2, "Consuming purchase with token: <redacted>
    L7353 [server/config field] invoke-virtual {v4}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L7402 [server/config field] invoke-virtual {v4}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L7522 [server/config field] invoke-virtual {v5}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L7731 [server/config field] invoke-virtual {v12}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L7747 [server/config field] invoke-virtual {v9}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L7760 [server/config field] invoke-virtual {v9}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L8307 [server/config field] invoke-virtual {v9}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L8363 [server/config field] invoke-virtual {v8}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L8676 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L8714 [server/config field] invoke-virtual {v2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L8783 [server/config field] invoke-virtual {v2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L8890 [server/config field] invoke-virtual {v2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L8959 [server/config field] invoke-virtual {v2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L9066 [server/config field] invoke-virtual {v2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L9137 [server/config field] invoke-virtual {v2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\android\billingclient\api\BillingFlowParams$SubscriptionUpdateParams$Builder.smali
    L123 [SDK/auth keyword] const-string v1, "Please provide Old SKU purchase information(token/id) or original external transaction id, not both."
    L146 [SDK/auth keyword] const-string v1, "Old SKU purchase information(token/id) or original external transaction id must be provided."

FILE: smali\com\android\billingclient\api\ConsumeParams$Builder.smali
    L63 [SDK/auth keyword] const-string v1, "Purchase token must be set"

FILE: smali\com\android\billingclient\api\ProductDetails.smali
    L568 [server/config field] const-string v1, "packageName"

FILE: smali\com\android\billingclient\api\ProxyBillingActivity.smali
    L57 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L116 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\android\billingclient\api\Purchase.smali
    L260 [server/config field] .method public getPackageName()Ljava/lang/String;
    L266 [server/config field] const-string v1, "packageName"
    L341 [SDK/auth keyword] const-string v1, "token"

FILE: smali\com\android\billingclient\api\PurchaseHistoryRecord.smali
    L232 [SDK/auth keyword] const-string v1, "token"

FILE: smali\com\android\billingclient\api\SkuDetails.smali
    L503 [server/config field] const-string v1, "packageName"

FILE: smali\com\android\billingclient\api\UserChoiceDetails$Product.smali
    L247 [SDK/auth keyword] const-string v0, "{id: %s, type: %s, offer token: <redacted>}"

FILE: smali\com\android\billingclient\api\zzay.smali
    L280 [server/config field] invoke-virtual {v5}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\android\billingclient\api\zzca.smali
    L243 [SDK/auth keyword] const-string v3, "Invalid purchase token."

FILE: smali\com\android\billingclient\api\zzcd.smali
    L375 [server/config field] invoke-virtual {p3}, Lcom/android/billingclient/api/Purchase;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\datatransport\backend\cct\BuildConfig.smali
    L11 [server/config field] .field public static final LIBRARY_PACKAGE_NAME:Ljava/lang/String; = "com.google.android.datatransport.backend.cct"

FILE: smali\com\google\android\datatransport\cct\CCTDestination.smali
    L40 [server/config field] .field private final endPoint:Ljava/lang/String;
    L147 [server/config field] iput-object p1, p0, Lcom/google/android/datatransport/cct/CCTDestination;->endPoint:Ljava/lang/String;
    L272 [server/config field] const-string v0, "Missing endpoint in CCTDestination extras"
    L309 [server/config field] iget-object v1, p0, Lcom/google/android/datatransport/cct/CCTDestination;->endPoint:Ljava/lang/String;
    L331 [server/config field] iget-object v3, p0, Lcom/google/android/datatransport/cct/CCTDestination;->endPoint:Ljava/lang/String;
    L380 [server/config field] .method public getEndPoint()Ljava/lang/String;
    L384 [server/config field] iget-object v0, p0, Lcom/google/android/datatransport/cct/CCTDestination;->endPoint:Ljava/lang/String;

FILE: smali\com\google\android\datatransport\cct\CctTransportBackend.smali
    L61 [SDK/auth keyword] .field private static final KEY_SDK_VERSION:Ljava/lang/String; = "sdk-version"
    L77 [server/config field] .field final endPoint:Ljava/net/URL;
    L142 [server/config field] iput-object p1, p0, Lcom/google/android/datatransport/cct/CctTransportBackend;->endPoint:Ljava/net/URL;
    L180 [HTTP/API client] check-cast v0, Ljava/net/HttpURLConnection;
    L185 [HTTP/API client] invoke-virtual {v0, v1}, Ljava/net/HttpURLConnection;->setConnectTimeout(I)V
    L190 [HTTP/API client] invoke-virtual {v0, v1}, Ljava/net/HttpURLConnection;->setReadTimeout(I)V
    L195 [HTTP/API client] invoke-virtual {v0, v1}, Ljava/net/HttpURLConnection;->setDoOutput(Z)V
    L200 [HTTP/API client] invoke-virtual {v0, v3}, Ljava/net/HttpURLConnection;->setInstanceFollowRedirects(Z)V
    L205 [HTTP/API client] invoke-virtual {v0, v4}, Ljava/net/HttpURLConnection;->setRequestMethod(Ljava/lang/String;)V
    L223 [HTTP/API client] invoke-virtual {v0, v3, v1}, Ljava/net/HttpURLConnection;->setRequestProperty(Ljava/lang/String;Ljava/lang/String;)V
    L230 [HTTP/API client] invoke-virtual {v0, v1, v3}, Ljava/net/HttpURLConnection;->setRequestProperty(Ljava/lang/String;Ljava/lang/String;)V
    L237 [HTTP/API client] invoke-virtual {v0, v5, v4}, Ljava/net/HttpURLConnection;->setRequestProperty(Ljava/lang/String;Ljava/lang/String;)V
    L242 [HTTP/API client] invoke-virtual {v0, v4, v3}, Ljava/net/HttpURLConnection;->setRequestProperty(Ljava/lang/String;Ljava/lang/String;)V
    L254 [HTTP/API client] invoke-virtual {v0, v3, v4}, Ljava/net/HttpURLConnection;->setRequestProperty(Ljava/lang/String;Ljava/lang/String;)V
    L263 [HTTP/API client] invoke-virtual {v0}, Ljava/net/HttpURLConnection;->getOutputStream()Ljava/io/OutputStream;
    L316 [HTTP/API client] invoke-virtual {v0}, Ljava/net/HttpURLConnection;->getResponseCode()I
    L332 [HTTP/API client] invoke-virtual {v0, v5}, Ljava/net/HttpURLConnection;->getHeaderField(Ljava/lang/String;)Ljava/lang/String;
    L341 [HTTP/API client] invoke-virtual {v0, v1}, Ljava/net/HttpURLConnection;->getHeaderField(Ljava/lang/String;)Ljava/lang/String;
    L375 [HTTP/API client] invoke-virtual {v0}, Ljava/net/HttpURLConnection;->getInputStream()Ljava/io/InputStream;
    L381 [HTTP/API client] invoke-virtual {v0, v1}, Ljava/net/HttpURLConnection;->getHeaderField(Ljava/lang/String;)Ljava/lang/String;
    L485 [HTTP/API client] invoke-virtual {v0, v1}, Ljava/net/HttpURLConnection;->getHeaderField(Ljava/lang/String;)Ljava/lang/String;
    L679 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L871 [SDK/auth keyword] const-string v6, "sdk-version"
    L1445 [SDK/auth keyword] const-string v1, "sdk-version"
    L1632 [server/config field] iget-object v1, p0, Lcom/google/android/datatransport/cct/CctTransportBackend;->endPoint:Ljava/net/URL;
    L1669 [server/config field] invoke-virtual {p1}, Lcom/google/android/datatransport/cct/CCTDestination;->getEndPoint()Ljava/lang/String;
    L1676 [server/config field] invoke-virtual {p1}, Lcom/google/android/datatransport/cct/CCTDestination;->getEndPoint()Ljava/lang/String;

FILE: smali\com\google\android\datatransport\runtime\BuildConfig.smali
    L11 [server/config field] .field public static final LIBRARY_PACKAGE_NAME:Ljava/lang/String; = "com.google.android.datatransport.runtime"

FILE: smali\com\google\android\datatransport\runtime\DaggerTransportRuntimeComponent.smali
    L49 [server/config field] .field private packageNameProvider:Ljavax/inject/Provider;
    L226 [server/config field] invoke-static {p1}, Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;->create(Ljavax/inject/Provider;)Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;
    L234 [server/config field] iput-object p1, p0, Lcom/google/android/datatransport/runtime/DaggerTransportRuntimeComponent;->packageNameProvider:Ljavax/inject/Provider;
    L251 [server/config field] iget-object v3, p0, Lcom/google/android/datatransport/runtime/DaggerTransportRuntimeComponent;->packageNameProvider:Ljavax/inject/Provider;

FILE: smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\JobInfoScheduler.smali
    L114 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\SchedulerConfig$Flag.smali
    L30 [identity/device field] .field public static final enum DEVICE_IDLE:Lcom/google/android/datatransport/runtime/scheduling/jobscheduling/SchedulerConfig$Flag;
    L53 [identity/device field] const-string v3, "DEVICE_IDLE"
    L59 [identity/device field] sput-object v1, Lcom/google/android/datatransport/runtime/scheduling/jobscheduling/SchedulerConfig$Flag;->DEVICE_IDLE:Lcom/google/android/datatransport/runtime/scheduling/jobscheduling/SchedulerConfig$Flag;

FILE: smali\com\google\android\datatransport\runtime\scheduling\jobscheduling\SchedulerConfig.smali
    L225 [identity/device field] sget-object v5, Lcom/google/android/datatransport/runtime/scheduling/jobscheduling/SchedulerConfig$Flag;->DEVICE_IDLE:Lcom/google/android/datatransport/runtime/scheduling/jobscheduling/SchedulerConfig$Flag;
    L338 [identity/device field] sget-object v0, Lcom/google/android/datatransport/runtime/scheduling/jobscheduling/SchedulerConfig$Flag;->DEVICE_IDLE:Lcom/google/android/datatransport/runtime/scheduling/jobscheduling/SchedulerConfig$Flag;
    L347 [identity/device field] invoke-virtual {p1, v1}, Landroid/app/job/JobInfo$Builder;->setRequiresDeviceIdle(Z)Landroid/app/job/JobInfo$Builder;

FILE: smali\com\google\android\datatransport\runtime\scheduling\persistence\EventStoreModule.smali
    L35 [server/config field] .method static packageName(Landroid/content/Context;)Ljava/lang/String;
    L41 [server/config field] value = "PACKAGE_NAME"
    L48 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\datatransport\runtime\scheduling\persistence\EventStoreModule_PackageNameFactory.smali
    L1 [server/config field] .class public final Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;
    L3 [server/config field] .source "EventStoreModule_PackageNameFactory.java"
    L48 [server/config field] iput-object p1, p0, Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;->contextProvider:Ljavax/inject/Provider;
    L53 [server/config field] .method public static create(Ljavax/inject/Provider;)Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;
    L61 [server/config field] "Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;"
    L66 [server/config field] new-instance v0, Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;
    L68 [server/config field] invoke-direct {v0, p0}, Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;-><init>(Ljavax/inject/Provider;)V
    L73 [server/config field] .method public static packageName(Landroid/content/Context;)Ljava/lang/String;
    L77 [server/config field] invoke-static {p0}, Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule;->packageName(Landroid/content/Context;)Ljava/lang/String;
    L98 [server/config field] invoke-virtual {p0}, Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;->get()Ljava/lang/String;
    L109 [server/config field] iget-object v0, p0, Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;->contextProvider:Ljavax/inject/Provider;
    L117 [server/config field] invoke-static {v0}, Lcom/google/android/datatransport/runtime/scheduling/persistence/EventStoreModule_PackageNameFactory;->packageName(Landroid/content/Context;)Ljava/lang/String;

FILE: smali\com\google\android\datatransport\runtime\scheduling\persistence\SQLiteEventStore.smali
    L39 [server/config field] .field private final packageName:Ljavax/inject/Provider;
    L74 [server/config field] value = "PACKAGE_NAME"
    L109 [server/config field] iput-object p5, p0, Lcom/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore;->packageName:Ljavax/inject/Provider;
    L2590 [server/config field] iget-object p1, p0, Lcom/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore;->packageName:Ljavax/inject/Provider;

FILE: smali\com\google\android\datatransport\runtime\scheduling\persistence\SQLiteEventStore_Factory.smali
    L41 [server/config field] .field private final packageNameProvider:Ljavax/inject/Provider;
    L112 [server/config field] iput-object p5, p0, Lcom/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore_Factory;->packageNameProvider:Ljavax/inject/Provider;
    L235 [server/config field] iget-object v4, p0, Lcom/google/android/datatransport/runtime/scheduling/persistence/SQLiteEventStore_Factory;->packageNameProvider:Ljavax/inject/Provider;

FILE: smali\com\google\android\gms\auth\api\signin\GoogleSignInAccount.smali
    L1 [SDK/auth keyword] .class public Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L1 [API route or URL] .class public Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L14 [SDK/auth keyword] "Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;",
    L14 [API route or URL] "Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;",
    L56 [SDK/auth keyword] new-instance v0, Lcom/google/android/gms/auth/api/signin/zab;
    L56 [API route or URL] new-instance v0, Lcom/google/android/gms/auth/api/signin/zab;
    L58 [SDK/auth keyword] invoke-direct {v0}, Lcom/google/android/gms/auth/api/signin/zab;-><init>()V
    L58 [API route or URL] invoke-direct {v0}, Lcom/google/android/gms/auth/api/signin/zab;-><init>()V
    L60 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->CREATOR:Landroid/os/Parcelable$Creator;
    L60 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->CREATOR:Landroid/os/Parcelable$Creator;
    L66 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaa:Lcom/google/android/gms/common/util/Clock;
    L66 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaa:Lcom/google/android/gms/common/util/Clock;
    L82 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zan:Ljava/util/Set;
    L82 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zan:Ljava/util/Set;
    L84 [SDK/auth keyword] iput p1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zab:I
    L84 [API route or URL] iput p1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zab:I
    L86 [SDK/auth keyword] iput-object p2, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zad:Ljava/lang/String;
    L86 [API route or URL] iput-object p2, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zad:Ljava/lang/String;
    L88 [SDK/auth keyword] iput-object p3, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zae:Ljava/lang/String;
    L88 [API route or URL] iput-object p3, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zae:Ljava/lang/String;
    L90 [SDK/auth keyword] iput-object p4, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaf:Ljava/lang/String;
    L90 [API route or URL] iput-object p4, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaf:Ljava/lang/String;
    L92 [SDK/auth keyword] iput-object p5, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zag:Ljava/lang/String;
    L92 [API route or URL] iput-object p5, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zag:Ljava/lang/String;
    L94 [SDK/auth keyword] iput-object p6, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zah:Landroid/net/Uri;
    L94 [API route or URL] iput-object p6, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zah:Landroid/net/Uri;
    L96 [SDK/auth keyword] iput-object p7, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zai:Ljava/lang/String;
    L96 [API route or URL] iput-object p7, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zai:Ljava/lang/String;
    L98 [SDK/auth keyword] iput-wide p8, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaj:J
    L98 [API route or URL] iput-wide p8, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaj:J
    L100 [SDK/auth keyword] iput-object p10, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zak:Ljava/lang/String;
    L100 [API route or URL] iput-object p10, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zak:Ljava/lang/String;
    L102 [SDK/auth keyword] iput-object p11, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zac:Ljava/util/List;
    L102 [API route or URL] iput-object p11, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zac:Ljava/util/List;
    L104 [SDK/auth keyword] iput-object p12, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zal:Ljava/lang/String;
    L104 [API route or URL] iput-object p12, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zal:Ljava/lang/String;
    L106 [SDK/auth keyword] iput-object p13, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zam:Ljava/lang/String;
    L106 [API route or URL] iput-object p13, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zam:Ljava/lang/String;
    L111 [SDK/auth keyword] .method public static createDefault()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L111 [API route or URL] .method public static createDefault()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L127 [SDK/auth keyword] invoke-static {v0, v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zae(Landroid/accounts/Account;Ljava/util/Set;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L127 [API route or URL] invoke-static {v0, v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zae(Landroid/accounts/Account;Ljava/util/Set;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L134 [SDK/auth keyword] .method public static fromAccount(Landroid/accounts/Account;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L134 [API route or URL] .method public static fromAccount(Landroid/accounts/Account;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L142 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zae(Landroid/accounts/Account;Ljava/util/Set;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L142 [API route or URL] invoke-static {p0, v0}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zae(Landroid/accounts/Account;Ljava/util/Set;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L149 [SDK/auth keyword] .method public static zaa(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/Long;Ljava/lang/String;Ljava/util/Set;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount...
    L149 [API route or URL] .method public static zaa(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/Long;Ljava/lang/String;Ljava/util/Set;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount...
    L153 [SDK/auth keyword] new-instance v14, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L153 [API route or URL] new-instance v14, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L195 [SDK/auth keyword] invoke-direct/range {v0 .. v13}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;-><init>(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;JLjava/lang/String;Ljava/util/List;Ljava/lang/Stri...
    L195 [API route or URL] invoke-direct/range {v0 .. v13}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;-><init>(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;JLjava/lang/String;Ljava/util/List;Ljava/lang/Stri...
    L200 [SDK/auth keyword] .method public static zab(Ljava/lang/String;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L200 [API route or URL] .method public static zab(Ljava/lang/String;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L432 [SDK/auth keyword] invoke-static/range {v2 .. v11}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaa(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/Long;Ljava/lang/String;Lj...
    L432 [API route or URL] invoke-static/range {v2 .. v11}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaa(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/Long;Ljava/lang/String;Lj...
    L450 [SDK/auth keyword] iput-object v1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zai:Ljava/lang/String;
    L450 [API route or URL] iput-object v1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zai:Ljava/lang/String;
    L455 [SDK/auth keyword] .method private static zae(Landroid/accounts/Account;Ljava/util/Set;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L455 [API route or URL] .method private static zae(Landroid/accounts/Account;Ljava/util/Set;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L485 [SDK/auth keyword] invoke-static/range {v0 .. v9}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaa(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/Long;Ljava/lang/String;Lja...
    L485 [API route or URL] invoke-static/range {v0 .. v9}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaa(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/Long;Ljava/lang/String;Lja...
    L512 [SDK/auth keyword] instance-of v2, p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L512 [API route or URL] instance-of v2, p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L519 [SDK/auth keyword] check-cast p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L519 [API route or URL] check-cast p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L521 [SDK/auth keyword] iget-object v2, p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zak:Ljava/lang/String;
    L521 [API route or URL] iget-object v2, p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zak:Ljava/lang/String;
    L523 [SDK/auth keyword] iget-object v3, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zak:Ljava/lang/String;
    L523 [API route or URL] iget-object v3, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zak:Ljava/lang/String;
    L533 [SDK/auth keyword] invoke-virtual {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->getRequestedScopes()Ljava/util/Set;
    L533 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->getRequestedScopes()Ljava/util/Set;
    L537 [SDK/auth keyword] invoke-virtual {p0}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->getRequestedScopes()Ljava/util/Set;
    L537 [API route or URL] invoke-virtual {p0}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->getRequestedScopes()Ljava/util/Set;
    L557 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaf:Ljava/lang/String;
    L557 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaf:Ljava/lang/String;
    L578 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zag:Ljava/lang/String;
    L578 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zag:Ljava/lang/String;
    L586 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaf:Ljava/lang/String;
    L586 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zaf:Ljava/lang/String;
    ... further matches omitted for this file

FILE: smali\com\google\android\gms\auth\api\signin\GoogleSignInOptions$Builder.smali
    L1 [SDK/auth keyword] .class public final Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L1 [API route or URL] .class public final Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L8 [SDK/auth keyword] value = Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L8 [API route or URL] value = Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L48 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L48 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L55 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zah:Ljava/util/Map;
    L55 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zah:Ljava/util/Map;
    L60 [SDK/auth keyword] .method public constructor <init>(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)V
    L60 [API route or URL] .method public constructor <init>(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)V
    L70 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L70 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L77 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zah:Ljava/util/Map;
    L77 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zah:Ljava/util/Map;
    L85 [SDK/auth keyword] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zah(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Ljava/util/ArrayList;
    L85 [API route or URL] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zah(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Ljava/util/ArrayList;
    L91 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L91 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L94 [SDK/auth keyword] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zal(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Z
    L94 [API route or URL] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zal(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Z
    L98 [SDK/auth keyword] iput-boolean v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zab:Z
    L98 [API route or URL] iput-boolean v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zab:Z
    L101 [SDK/auth keyword] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaj(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Z
    L101 [API route or URL] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaj(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Z
    L105 [SDK/auth keyword] iput-boolean v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zac:Z
    L105 [API route or URL] iput-boolean v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zac:Z
    L108 [SDK/auth keyword] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zak(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Z
    L108 [API route or URL] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zak(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Z
    L112 [SDK/auth keyword] iput-boolean v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zad:Z
    L112 [API route or URL] iput-boolean v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zad:Z
    L115 [SDK/auth keyword] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zae(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Ljava/lang/String;
    L115 [API route or URL] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zae(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Ljava/lang/String;
    L119 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zae:Ljava/lang/String;
    L119 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zae:Ljava/lang/String;
    L122 [SDK/auth keyword] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaa(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Landroid/accounts/Account;
    L122 [API route or URL] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaa(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Landroid/accounts/Account;
    L126 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaf:Landroid/accounts/Account;
    L126 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaf:Landroid/accounts/Account;
    L129 [SDK/auth keyword] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zac(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Ljava/lang/String;
    L129 [API route or URL] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zac(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Ljava/lang/String;
    L133 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zag:Ljava/lang/String;
    L133 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zag:Ljava/lang/String;
    L136 [SDK/auth keyword] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zag(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Ljava/util/ArrayList;
    L136 [API route or URL] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zag(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Ljava/util/ArrayList;
    L140 [SDK/auth keyword] invoke-static {v0}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zai(Ljava/util/List;)Ljava/util/Map;
    L140 [API route or URL] invoke-static {v0}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zai(Ljava/util/List;)Ljava/util/Map;
    L144 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zah:Ljava/util/Map;
    L144 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zah:Ljava/util/Map;
    L147 [SDK/auth keyword] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zad(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Ljava/lang/String;
    L147 [API route or URL] invoke-static {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zad(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)Ljava/lang/String;
    L151 [SDK/auth keyword] iput-object p1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zai:Ljava/lang/String;
    L151 [API route or URL] iput-object p1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zai:Ljava/lang/String;
    L162 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zae:Ljava/lang/String;
    L162 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zae:Ljava/lang/String;
    L192 [SDK/auth keyword] .method public addExtension(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;)Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L192 [API route or URL] .method public addExtension(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;)Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L196 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zah:Ljava/util/Map;
    L196 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zah:Ljava/util/Map;
    L198 [SDK/auth keyword] invoke-interface {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;->getExtensionType()I
    L198 [API route or URL] invoke-interface {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;->getExtensionType()I
    L213 [SDK/auth keyword] invoke-interface {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;->getImpliedScopes()Ljava/util/List;
    L213 [API route or URL] invoke-interface {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;->getImpliedScopes()Ljava/util/List;
    L219 [SDK/auth keyword] iget-object v1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L219 [API route or URL] iget-object v1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L225 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zah:Ljava/util/Map;
    L225 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zah:Ljava/util/Map;
    L228 [SDK/auth keyword] invoke-interface {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;->getExtensionType()I
    L228 [API route or URL] invoke-interface {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;->getExtensionType()I
    L236 [SDK/auth keyword] new-instance v2, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;
    L236 [API route or URL] new-instance v2, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;
    L238 [SDK/auth keyword] invoke-direct {v2, p1}, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;-><init>(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;)V
    L238 [API route or URL] invoke-direct {v2, p1}, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;-><init>(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;)V
    L257 [SDK/auth keyword] .method public build()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L257 [API route or URL] .method public build()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L261 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L261 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L263 [SDK/auth keyword] sget-object v1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zae:Lcom/google/android/gms/common/api/Scope;
    L263 [API route or URL] sget-object v1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zae:Lcom/google/android/gms/common/api/Scope;
    L271 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    L271 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->zaa:Ljava/util/Set;
    ... further matches omitted for this file

FILE: smali\com\google\android\gms\auth\api\signin\GoogleSignInOptions.smali
    L1 [SDK/auth keyword] .class public Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L1 [API route or URL] .class public Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L13 [SDK/auth keyword] Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L13 [API route or URL] Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L23 [SDK/auth keyword] "Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;",
    L23 [API route or URL] "Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;",
    L29 [SDK/auth keyword] .field public static final DEFAULT_GAMES_SIGN_IN:Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L29 [API route or URL] .field public static final DEFAULT_GAMES_SIGN_IN:Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L31 [SDK/auth keyword] .field public static final DEFAULT_SIGN_IN:Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L31 [API route or URL] .field public static final DEFAULT_SIGN_IN:Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L81 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaa:Lcom/google/android/gms/common/api/Scope;
    L81 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaa:Lcom/google/android/gms/common/api/Scope;
    L90 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zab:Lcom/google/android/gms/common/api/Scope;
    L90 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zab:Lcom/google/android/gms/common/api/Scope;
    L99 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zac:Lcom/google/android/gms/common/api/Scope;
    L99 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zac:Lcom/google/android/gms/common/api/Scope;
    L103 [SDK/auth keyword] const-string v1, "https://www.googleapis.com/auth/games_lite"
    L103 [API route or URL] const-string v1, "https://www.googleapis.com/auth/games_lite"
    L108 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zad:Lcom/google/android/gms/common/api/Scope;
    L108 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zad:Lcom/google/android/gms/common/api/Scope;
    L112 [SDK/auth keyword] const-string v2, "https://www.googleapis.com/auth/games"
    L112 [API route or URL] const-string v2, "https://www.googleapis.com/auth/games"
    L117 [SDK/auth keyword] sput-object v1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zae:Lcom/google/android/gms/common/api/Scope;
    L117 [API route or URL] sput-object v1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zae:Lcom/google/android/gms/common/api/Scope;
    L119 [SDK/auth keyword] new-instance v1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L119 [API route or URL] new-instance v1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L122 [SDK/auth keyword] invoke-direct {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;-><init>()V
    L122 [API route or URL] invoke-direct {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;-><init>()V
    L125 [SDK/auth keyword] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->requestId()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L125 [API route or URL] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->requestId()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L127 [SDK/auth keyword] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->requestProfile()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L127 [API route or URL] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->requestProfile()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L129 [SDK/auth keyword] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->build()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L129 [API route or URL] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->build()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L133 [SDK/auth keyword] sput-object v1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->DEFAULT_SIGN_IN:Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L133 [API route or URL] sput-object v1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->DEFAULT_SIGN_IN:Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L135 [SDK/auth keyword] new-instance v1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L135 [API route or URL] new-instance v1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;
    L138 [SDK/auth keyword] invoke-direct {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;-><init>()V
    L138 [API route or URL] invoke-direct {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;-><init>()V
    L145 [SDK/auth keyword] invoke-virtual {v1, v0, v2}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->requestScopes(Lcom/google/android/gms/common/api/Scope;[Lcom/google/android/gms/common/api/Scope;)Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Bui...
    L145 [API route or URL] invoke-virtual {v1, v0, v2}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->requestScopes(Lcom/google/android/gms/common/api/Scope;[Lcom/google/android/gms/common/api/Scope;)Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Bui...
    L147 [SDK/auth keyword] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->build()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L147 [API route or URL] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions$Builder;->build()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L151 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->DEFAULT_GAMES_SIGN_IN:Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L151 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->DEFAULT_GAMES_SIGN_IN:Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L153 [SDK/auth keyword] new-instance v0, Lcom/google/android/gms/auth/api/signin/zae;
    L153 [API route or URL] new-instance v0, Lcom/google/android/gms/auth/api/signin/zae;
    L155 [SDK/auth keyword] invoke-direct {v0}, Lcom/google/android/gms/auth/api/signin/zae;-><init>()V
    L155 [API route or URL] invoke-direct {v0}, Lcom/google/android/gms/auth/api/signin/zae;-><init>()V
    L157 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->CREATOR:Landroid/os/Parcelable$Creator;
    L157 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->CREATOR:Landroid/os/Parcelable$Creator;
    L159 [SDK/auth keyword] new-instance v0, Lcom/google/android/gms/auth/api/signin/zac;
    L159 [API route or URL] new-instance v0, Lcom/google/android/gms/auth/api/signin/zac;
    L161 [SDK/auth keyword] invoke-direct {v0}, Lcom/google/android/gms/auth/api/signin/zac;-><init>()V
    L161 [API route or URL] invoke-direct {v0}, Lcom/google/android/gms/auth/api/signin/zac;-><init>()V
    L163 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zag:Ljava/util/Comparator;
    L163 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zag:Ljava/util/Comparator;
    L172 [SDK/auth keyword] invoke-static/range {p9 .. p9}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zam(Ljava/util/List;)Ljava/util/Map;
    L172 [API route or URL] invoke-static/range {p9 .. p9}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zam(Ljava/util/List;)Ljava/util/Map;
    L197 [SDK/auth keyword] invoke-direct/range {v0 .. v10}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;-><init>(ILjava/util/ArrayList;Landroid/accounts/Account;ZZZLjava/lang/String;Ljava/lang/String;Ljava/util/Map;Ljava/lang/String;)V
    L197 [API route or URL] invoke-direct/range {v0 .. v10}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;-><init>(ILjava/util/ArrayList;Landroid/accounts/Account;ZZZLjava/lang/String;Ljava/lang/String;Ljava/util/Map;Ljava/lang/String;)V
    L208 [SDK/auth keyword] iput p1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaf:I
    L208 [API route or URL] iput p1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaf:I
    L210 [SDK/auth keyword] iput-object p2, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zah:Ljava/util/ArrayList;
    L210 [API route or URL] iput-object p2, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zah:Ljava/util/ArrayList;
    L212 [SDK/auth keyword] iput-object p3, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zai:Landroid/accounts/Account;
    L212 [API route or URL] iput-object p3, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zai:Landroid/accounts/Account;
    L214 [SDK/auth keyword] iput-boolean p4, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaj:Z
    L214 [API route or URL] iput-boolean p4, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaj:Z
    L216 [SDK/auth keyword] iput-boolean p5, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zak:Z
    L216 [API route or URL] iput-boolean p5, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zak:Z
    L218 [SDK/auth keyword] iput-boolean p6, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zal:Z
    L218 [API route or URL] iput-boolean p6, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zal:Z
    L220 [SDK/auth keyword] iput-object p7, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zam:Ljava/lang/String;
    L220 [API route or URL] iput-object p7, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zam:Ljava/lang/String;
    L222 [SDK/auth keyword] iput-object p8, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zan:Ljava/lang/String;
    L222 [API route or URL] iput-object p8, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zan:Ljava/lang/String;
    L233 [SDK/auth keyword] iput-object p1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zao:Ljava/util/ArrayList;
    L233 [API route or URL] iput-object p1, p0, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zao:Ljava/util/ArrayList;
    ... further matches omitted for this file

FILE: smali\com\google\android\gms\auth\api\signin\GoogleSignInOptionsExtension.smali
    L1 [SDK/auth keyword] .class public interface abstract Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;
    L1 [API route or URL] .class public interface abstract Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;

FILE: smali\com\google\android\gms\auth\api\signin\internal\GoogleSignInOptionsExtensionParcelable.smali
    L1 [SDK/auth keyword] .class public Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;
    L1 [API route or URL] .class public Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;
    L11 [SDK/auth keyword] "Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;",
    L11 [API route or URL] "Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;",
    L30 [SDK/auth keyword] new-instance v0, Lcom/google/android/gms/auth/api/signin/internal/zaa;
    L30 [API route or URL] new-instance v0, Lcom/google/android/gms/auth/api/signin/internal/zaa;
    L32 [SDK/auth keyword] invoke-direct {v0}, Lcom/google/android/gms/auth/api/signin/internal/zaa;-><init>()V
    L32 [API route or URL] invoke-direct {v0}, Lcom/google/android/gms/auth/api/signin/internal/zaa;-><init>()V
    L34 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->CREATOR:Landroid/os/Parcelable$Creator;
    L34 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->CREATOR:Landroid/os/Parcelable$Creator;
    L45 [SDK/auth keyword] iput p1, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zaa:I
    L45 [API route or URL] iput p1, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zaa:I
    L47 [SDK/auth keyword] iput p2, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zab:I
    L47 [API route or URL] iput p2, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zab:I
    L49 [SDK/auth keyword] iput-object p3, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zac:Landroid/os/Bundle;
    L49 [API route or URL] iput-object p3, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zac:Landroid/os/Bundle;
    L54 [SDK/auth keyword] .method public constructor <init>(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;)V
    L54 [API route or URL] .method public constructor <init>(Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;)V
    L58 [SDK/auth keyword] invoke-interface {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;->getExtensionType()I
    L58 [API route or URL] invoke-interface {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;->getExtensionType()I
    L62 [SDK/auth keyword] invoke-interface {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;->toBundle()Landroid/os/Bundle;
    L62 [API route or URL] invoke-interface {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptionsExtension;->toBundle()Landroid/os/Bundle;
    L68 [SDK/auth keyword] invoke-direct {p0, v1, v0, p1}, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;-><init>(IILandroid/os/Bundle;)V
    L68 [API route or URL] invoke-direct {p0, v1, v0, p1}, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;-><init>(IILandroid/os/Bundle;)V
    L78 [SDK/auth keyword] iget v0, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zab:I
    L78 [API route or URL] iget v0, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zab:I
    L93 [SDK/auth keyword] iget v1, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zaa:I
    L93 [API route or URL] iget v1, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zaa:I
    L101 [SDK/auth keyword] invoke-virtual {p0}, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->getType()I
    L101 [API route or URL] invoke-virtual {p0}, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->getType()I
    L108 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zac:Landroid/os/Bundle;
    L108 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->zac:Landroid/os/Bundle;

FILE: smali\com\google\android\gms\auth\api\signin\internal\HashAccumulator.smali
    L1 [SDK/auth keyword] .class public Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;
    L1 [API route or URL] .class public Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;
    L18 [SDK/auth keyword] iput v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L18 [API route or URL] iput v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L25 [SDK/auth keyword] .method public addObject(Ljava/lang/Object;)Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;
    L25 [API route or URL] .method public addObject(Ljava/lang/Object;)Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;
    L29 [SDK/auth keyword] iget v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L29 [API route or URL] iget v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L47 [SDK/auth keyword] iput v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L47 [API route or URL] iput v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L55 [SDK/auth keyword] iget v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L55 [API route or URL] iget v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L60 [SDK/auth keyword] .method public final zaa(Z)Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;
    L60 [API route or URL] .method public final zaa(Z)Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;
    L63 [SDK/auth keyword] iget v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L63 [API route or URL] iget v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L69 [SDK/auth keyword] iput v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I
    L69 [API route or URL] iput v0, p0, Lcom/google/android/gms/auth/api/signin/internal/HashAccumulator;->zaa:I

FILE: smali\com\google\android\gms\auth\api\signin\internal\Storage.smali
    L1 [SDK/auth keyword] .class public Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L1 [API route or URL] .class public Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L9 [SDK/auth keyword] .field private static zab:Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L9 [API route or URL] .field private static zab:Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L27 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa:Ljava/util/concurrent/locks/Lock;
    L27 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa:Ljava/util/concurrent/locks/Lock;
    L42 [SDK/auth keyword] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac:Ljava/util/concurrent/locks/Lock;
    L42 [API route or URL] iput-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac:Ljava/util/concurrent/locks/Lock;
    L53 [SDK/auth keyword] iput-object p1, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zad:Landroid/content/SharedPreferences;
    L53 [API route or URL] iput-object p1, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zad:Landroid/content/SharedPreferences;
    L58 [SDK/auth keyword] .method public static getInstance(Landroid/content/Context;)Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L58 [API route or URL] .method public static getInstance(Landroid/content/Context;)Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L64 [SDK/auth keyword] sget-object v0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa:Ljava/util/concurrent/locks/Lock;
    L64 [API route or URL] sget-object v0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa:Ljava/util/concurrent/locks/Lock;
    L70 [SDK/auth keyword] sget-object v1, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zab:Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L70 [API route or URL] sget-object v1, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zab:Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L74 [SDK/auth keyword] new-instance v1, Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L74 [API route or URL] new-instance v1, Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L81 [SDK/auth keyword] invoke-direct {v1, p0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;-><init>(Landroid/content/Context;)V
    L81 [API route or URL] invoke-direct {v1, p0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;-><init>(Landroid/content/Context;)V
    L83 [SDK/auth keyword] sput-object v1, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zab:Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L83 [API route or URL] sput-object v1, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zab:Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L86 [SDK/auth keyword] sget-object p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zab:Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L86 [API route or URL] sget-object p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zab:Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L99 [SDK/auth keyword] sget-object v0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa:Ljava/util/concurrent/locks/Lock;
    L99 [API route or URL] sget-object v0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa:Ljava/util/concurrent/locks/Lock;
    L137 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac:Ljava/util/concurrent/locks/Lock;
    L137 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac:Ljava/util/concurrent/locks/Lock;
    L142 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zad:Landroid/content/SharedPreferences;
    L142 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zad:Landroid/content/SharedPreferences;
    L158 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac:Ljava/util/concurrent/locks/Lock;
    L158 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac:Ljava/util/concurrent/locks/Lock;
    L169 [SDK/auth keyword] iget-object v1, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac:Ljava/util/concurrent/locks/Lock;
    L169 [API route or URL] iget-object v1, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac:Ljava/util/concurrent/locks/Lock;
    L178 [SDK/auth keyword] .method public getSavedDefaultGoogleSignInAccount()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L178 [API route or URL] .method public getSavedDefaultGoogleSignInAccount()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L184 [SDK/auth keyword] invoke-virtual {p0, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa(Ljava/lang/String;)Ljava/lang/String;
    L184 [API route or URL] invoke-virtual {p0, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa(Ljava/lang/String;)Ljava/lang/String;
    L203 [SDK/auth keyword] invoke-static {v1, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zae(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    L203 [API route or URL] invoke-static {v1, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zae(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    L207 [SDK/auth keyword] invoke-virtual {p0, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa(Ljava/lang/String;)Ljava/lang/String;
    L207 [API route or URL] invoke-virtual {p0, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa(Ljava/lang/String;)Ljava/lang/String;
    L215 [SDK/auth keyword] invoke-static {v0}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zab(Ljava/lang/String;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L215 [API route or URL] invoke-static {v0}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zab(Ljava/lang/String;)Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L227 [SDK/auth keyword] .method public getSavedDefaultGoogleSignInOptions()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L227 [API route or URL] .method public getSavedDefaultGoogleSignInOptions()Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L233 [SDK/auth keyword] invoke-virtual {p0, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa(Ljava/lang/String;)Ljava/lang/String;
    L233 [API route or URL] invoke-virtual {p0, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa(Ljava/lang/String;)Ljava/lang/String;
    L252 [SDK/auth keyword] invoke-static {v1, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zae(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    L252 [API route or URL] invoke-static {v1, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zae(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    L256 [SDK/auth keyword] invoke-virtual {p0, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa(Ljava/lang/String;)Ljava/lang/String;
    L256 [API route or URL] invoke-virtual {p0, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa(Ljava/lang/String;)Ljava/lang/String;
    L264 [SDK/auth keyword] invoke-static {v0}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zab(Ljava/lang/String;)Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L264 [API route or URL] invoke-static {v0}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zab(Ljava/lang/String;)Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L276 [identity/device field] .method public getSavedRefreshToken()Ljava/lang/String;
    L279 [identity/device field] const-string v0, "refreshToken"
    L282 [SDK/auth keyword] invoke-virtual {p0, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa(Ljava/lang/String;)Ljava/lang/String;
    L282 [API route or URL] invoke-virtual {p0, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zaa(Ljava/lang/String;)Ljava/lang/String;
    L289 [SDK/auth keyword] .method public saveDefaultGoogleSignInAccount(Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)V
    L289 [API route or URL] .method public saveDefaultGoogleSignInAccount(Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;)V
    L301 [SDK/auth keyword] invoke-virtual {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zac()Ljava/lang/String;
    L301 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zac()Ljava/lang/String;
    L306 [SDK/auth keyword] invoke-virtual {p0, v0, v1}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zad(Ljava/lang/String;Ljava/lang/String;)V
    L306 [API route or URL] invoke-virtual {p0, v0, v1}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zad(Ljava/lang/String;Ljava/lang/String;)V
    L315 [SDK/auth keyword] invoke-virtual {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zac()Ljava/lang/String;
    L315 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zac()Ljava/lang/String;
    L322 [SDK/auth keyword] invoke-static {v1, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zae(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    L322 [API route or URL] invoke-static {v1, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zae(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    L326 [SDK/auth keyword] invoke-virtual {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zad()Ljava/lang/String;
    L326 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->zad()Ljava/lang/String;
    L331 [SDK/auth keyword] invoke-virtual {p0, v1, p1}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zad(Ljava/lang/String;Ljava/lang/String;)V
    L331 [API route or URL] invoke-virtual {p0, v1, p1}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zad(Ljava/lang/String;Ljava/lang/String;)V
    L336 [SDK/auth keyword] invoke-static {p1, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zae(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    L336 [API route or URL] invoke-static {p1, v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zae(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    L340 [SDK/auth keyword] invoke-virtual {p2}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaf()Ljava/lang/String;
    L340 [API route or URL] invoke-virtual {p2}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;->zaf()Ljava/lang/String;
    L344 [SDK/auth keyword] invoke-virtual {p0, p1, p2}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zad(Ljava/lang/String;Ljava/lang/String;)V
    L344 [API route or URL] invoke-virtual {p0, p1, p2}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zad(Ljava/lang/String;Ljava/lang/String;)V
    L353 [SDK/auth keyword] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac:Ljava/util/concurrent/locks/Lock;
    L353 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac:Ljava/util/concurrent/locks/Lock;
    ... further matches omitted for this file

FILE: smali\com\google\android\gms\auth\api\signin\internal\zaa.smali
    L1 [SDK/auth keyword] .class public final Lcom/google/android/gms/auth/api/signin/internal/zaa;
    L1 [API route or URL] .class public final Lcom/google/android/gms/auth/api/signin/internal/zaa;
    L98 [SDK/auth keyword] new-instance p1, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;
    L98 [API route or URL] new-instance p1, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;
    L100 [SDK/auth keyword] invoke-direct {p1, v2, v3, v1}, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;-><init>(IILandroid/os/Bundle;)V
    L100 [API route or URL] invoke-direct {p1, v2, v3, v1}, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;-><init>(IILandroid/os/Bundle;)V
    L109 [SDK/auth keyword] new-array p1, p1, [Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;
    L109 [API route or URL] new-array p1, p1, [Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;

FILE: smali\com\google\android\gms\auth\api\signin\zaa.smali
    L1 [SDK/auth keyword] .class public final synthetic Lcom/google/android/gms/auth/api/signin/zaa;
    L1 [API route or URL] .class public final synthetic Lcom/google/android/gms/auth/api/signin/zaa;
    L10 [SDK/auth keyword] .field public static final synthetic zaa:Lcom/google/android/gms/auth/api/signin/zaa;
    L10 [API route or URL] .field public static final synthetic zaa:Lcom/google/android/gms/auth/api/signin/zaa;
    L17 [SDK/auth keyword] new-instance v0, Lcom/google/android/gms/auth/api/signin/zaa;
    L17 [API route or URL] new-instance v0, Lcom/google/android/gms/auth/api/signin/zaa;
    L19 [SDK/auth keyword] invoke-direct {v0}, Lcom/google/android/gms/auth/api/signin/zaa;-><init>()V
    L19 [API route or URL] invoke-direct {v0}, Lcom/google/android/gms/auth/api/signin/zaa;-><init>()V
    L21 [SDK/auth keyword] sput-object v0, Lcom/google/android/gms/auth/api/signin/zaa;->zaa:Lcom/google/android/gms/auth/api/signin/zaa;
    L21 [API route or URL] sput-object v0, Lcom/google/android/gms/auth/api/signin/zaa;->zaa:Lcom/google/android/gms/auth/api/signin/zaa;
    L43 [SDK/auth keyword] sget-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->CREATOR:Landroid/os/Parcelable$Creator;
    L43 [API route or URL] sget-object v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->CREATOR:Landroid/os/Parcelable$Creator;

FILE: smali\com\google\android\gms\auth\api\signin\zab.smali
    L1 [SDK/auth keyword] .class public final Lcom/google/android/gms/auth/api/signin/zab;
    L1 [API route or URL] .class public final Lcom/google/android/gms/auth/api/signin/zab;
    L217 [SDK/auth keyword] new-instance v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L217 [API route or URL] new-instance v0, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L221 [SDK/auth keyword] invoke-direct/range {v6 .. v19}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;-><init>(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;JLjava/lang/String;Ljava/util/List;Ljava/lang/Stri...
    L221 [API route or URL] invoke-direct/range {v6 .. v19}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;-><init>(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;JLjava/lang/String;Ljava/util/List;Ljava/lang/Stri...
    L248 [SDK/auth keyword] new-array p1, p1, [Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L248 [API route or URL] new-array p1, p1, [Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;

FILE: smali\com\google\android\gms\auth\api\signin\zac.smali
    L1 [SDK/auth keyword] .class final Lcom/google/android/gms/auth/api/signin/zac;
    L1 [API route or URL] .class final Lcom/google/android/gms/auth/api/signin/zac;

FILE: smali\com\google\android\gms\auth\api\signin\zad.smali
    L1 [SDK/auth keyword] .class public final synthetic Lcom/google/android/gms/auth/api/signin/zad;
    L1 [API route or URL] .class public final synthetic Lcom/google/android/gms/auth/api/signin/zad;

FILE: smali\com\google\android\gms\auth\api\signin\zae.smali
    L1 [SDK/auth keyword] .class public final Lcom/google/android/gms/auth/api/signin/zae;
    L1 [API route or URL] .class public final Lcom/google/android/gms/auth/api/signin/zae;
    L87 [SDK/auth keyword] sget-object v2, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->CREATOR:Landroid/os/Parcelable$Creator;
    L87 [API route or URL] sget-object v2, Lcom/google/android/gms/auth/api/signin/internal/GoogleSignInOptionsExtensionParcelable;->CREATOR:Landroid/os/Parcelable$Creator;
    L174 [SDK/auth keyword] new-instance p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L174 [API route or URL] new-instance p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L178 [SDK/auth keyword] invoke-direct/range {v3 .. v13}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;-><init>(ILjava/util/ArrayList;Landroid/accounts/Account;ZZZLjava/lang/String;Ljava/lang/String;Ljava/util/ArrayList;Ljava/lang/String;)V
    L178 [API route or URL] invoke-direct/range {v3 .. v13}, Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;-><init>(ILjava/util/ArrayList;Landroid/accounts/Account;ZZZLjava/lang/String;Ljava/lang/String;Ljava/util/ArrayList;Ljava/lang/String;)V
    L201 [SDK/auth keyword] new-array p1, p1, [Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;
    L201 [API route or URL] new-array p1, p1, [Lcom/google/android/gms/auth/api/signin/GoogleSignInOptions;

FILE: smali\com\google\android\gms\common\api\Api$ApiOptions$HasGoogleSignInAccountOptions.smali
    L21 [SDK/auth keyword] .method public abstract getGoogleSignInAccount()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L21 [API route or URL] .method public abstract getGoogleSignInAccount()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;

FILE: smali\com\google\android\gms\common\api\Api$Client.smali
    L36 [server/config field] .method public abstract getEndpointPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\common\api\BatchResult.smali
    L70 [SDK/auth keyword] const-string v1, "The result token does not belong to this batch"

FILE: smali\com\google\android\gms\common\api\GoogleApi.smali
    L431 [SDK/auth keyword] invoke-interface {v1}, Lcom/google/android/gms/common/api/Api$ApiOptions$HasGoogleSignInAccountOptions;->getGoogleSignInAccount()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L431 [API route or URL] invoke-interface {v1}, Lcom/google/android/gms/common/api/Api$ApiOptions$HasGoogleSignInAccountOptions;->getGoogleSignInAccount()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L438 [SDK/auth keyword] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->getAccount()Landroid/accounts/Account;
    L438 [API route or URL] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->getAccount()Landroid/accounts/Account;
    L478 [SDK/auth keyword] invoke-interface {v1}, Lcom/google/android/gms/common/api/Api$ApiOptions$HasGoogleSignInAccountOptions;->getGoogleSignInAccount()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L478 [API route or URL] invoke-interface {v1}, Lcom/google/android/gms/common/api/Api$ApiOptions$HasGoogleSignInAccountOptions;->getGoogleSignInAccount()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L493 [SDK/auth keyword] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->getRequestedScopes()Ljava/util/Set;
    L493 [API route or URL] invoke-virtual {v1}, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->getRequestedScopes()Ljava/util/Set;
    L525 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L529 [server/config field] invoke-virtual {v0, v1}, Lcom/google/android/gms/common/internal/ClientSettings$Builder;->setRealClientPackageName(Ljava/lang/String;)Lcom/google/android/gms/common/internal/ClientSettings$Builder;
    L657 [API route or URL] .method public doRegisterEventListener(Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;Lcom/google/android/gms/common/api/internal/UnregisterListenerMethod;)Lcom/google/android/gms/tasks/Task;
    L667 [API route or URL] "Lcom/google/android/gms/common/api/internal/RegisterListenerMethod<",
    L687 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->getListenerKey()Lcom/google/android/gms/common/api/internal/ListenerHolder$ListenerKey;
    L705 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->getListenerKey()Lcom/google/android/gms/common/api/internal/ListenerHolder$ListenerKey;
    L727 [API route or URL] invoke-virtual {v1, p0, p1, p2, v0}, Lcom/google/android/gms/common/api/internal/GoogleApiManager;->zao(Lcom/google/android/gms/common/api/GoogleApi;Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;Lcom/google/android/gms/common/api/internal/...
    L756 [SDK/auth keyword] iget-object v0, p1, Lcom/google/android/gms/common/api/internal/RegistrationMethods;->register:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L756 [API route or URL] iget-object v0, p1, Lcom/google/android/gms/common/api/internal/RegistrationMethods;->register:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L759 [API route or URL] invoke-virtual {v0}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->getListenerKey()Lcom/google/android/gms/common/api/internal/ListenerHolder$ListenerKey;
    L778 [SDK/auth keyword] iget-object v0, p1, Lcom/google/android/gms/common/api/internal/RegistrationMethods;->register:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L778 [API route or URL] iget-object v0, p1, Lcom/google/android/gms/common/api/internal/RegistrationMethods;->register:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L786 [API route or URL] invoke-virtual {v2, p0, v0, v1, p1}, Lcom/google/android/gms/common/api/internal/GoogleApiManager;->zao(Lcom/google/android/gms/common/api/GoogleApi;Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;Lcom/google/android/gms/common/api/internal/...

FILE: smali\com\google\android\gms\common\api\GoogleApiActivity.smali
    L42 [identity/device field] const-string p0, "failing_client_id"
    L194 [identity/device field] const-string v3, "failing_client_id"
    L346 [identity/device field] const-string v1, "failing_client_id"

FILE: smali\com\google\android\gms\common\api\GoogleApiClient$Builder.smali
    L132 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L897 [identity/device field] const-string v1, "clientId must be non-negative"

FILE: smali\com\google\android\gms\common\api\internal\GoogleApiManager.smali
    L1431 [server/config field] invoke-interface {v3}, Lcom/google/android/gms/common/api/Api$Client;->getEndpointPackageName()Ljava/lang/String;
    L1819 [API route or URL] .method public final zao(Lcom/google/android/gms/common/api/GoogleApi;Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;Lcom/google/android/gms/common/api/internal/UnregisterListenerMethod;Ljava/lang/Runnable;)Lcom/google/android/gms/tasks/Tas...
    L1828 [API route or URL] invoke-virtual {p2}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zaa()I
    L1839 [API route or URL] invoke-direct {v2, p2, p3, p4}, Lcom/google/android/gms/common/api/internal/zaci;-><init>(Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;Lcom/google/android/gms/common/api/internal/UnregisterListenerMethod;Ljava/lang/Runnable;)V

FILE: smali\com\google\android\gms\common\api\internal\GoogleServices.smali
    L54 [server/config field] invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getResourcePackageName(I)Ljava/lang/String;
    L120 [server/config field] const-string p1, "google_app_id"
    L139 [server/config field] const-string v1, "Missing google app id value from from string resources with name google_app_id."
    L260 [server/config field] .method public static getGoogleAppId()Ljava/lang/String;
    L263 [server/config field] const-string v0, "getGoogleAppId"
    L345 [server/config field] invoke-virtual {v0, p1}, Lcom/google/android/gms/common/api/internal/GoogleServices;->checkGoogleAppId(Ljava/lang/String;)Lcom/google/android/gms/common/api/Status;
    L428 [server/config field] .method checkGoogleAppId(Ljava/lang/String;)Lcom/google/android/gms/common/api/Status;

FILE: smali\com\google\android\gms\common\api\internal\LifecycleCallback.smali
    L27 [SDK/auth keyword] const-string v0, "Method not available in SDK."

FILE: smali\com\google\android\gms\common\api\internal\NonGmsServiceBrokerClient.smali
    L373 [server/config field] .method public final getEndpointPackageName()Ljava/lang/String;
    L391 [server/config field] invoke-virtual {v0}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\common\api\internal\RegisterListenerMethod.smali
    L1 [API route or URL] .class public abstract Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L46 [API route or URL] invoke-direct {p0, p1, v0, v1, v1}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;-><init>(Lcom/google/android/gms/common/api/internal/ListenerHolder;[Lcom/google/android/gms/common/Feature;ZI)V
    L68 [API route or URL] invoke-direct {p0, p1, p2, p3, v0}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;-><init>(Lcom/google/android/gms/common/api/internal/ListenerHolder;[Lcom/google/android/gms/common/Feature;ZI)V
    L89 [API route or URL] iput-object p1, p0, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zaa:Lcom/google/android/gms/common/api/internal/ListenerHolder;
    L91 [API route or URL] iput-object p2, p0, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zab:[Lcom/google/android/gms/common/Feature;
    L93 [API route or URL] iput-boolean p3, p0, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zac:Z
    L95 [API route or URL] iput p4, p0, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zad:I
    L106 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zaa:Lcom/google/android/gms/common/api/internal/ListenerHolder;
    L126 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zaa:Lcom/google/android/gms/common/api/internal/ListenerHolder;
    L138 [API route or URL] iget-object v0, p0, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zab:[Lcom/google/android/gms/common/Feature;
    L163 [API route or URL] iget v0, p0, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zad:I
    L171 [API route or URL] iget-boolean v0, p0, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zac:Z

FILE: smali\com\google\android\gms\common\api\internal\RegistrationMethods$Builder.smali
    L123 [SDK/auth keyword] const-string v3, "Must set register function"
    L201 [API route or URL] invoke-direct {v1, v8, v2, v0, v3}, Lcom/google/android/gms/common/api/internal/RegistrationMethods;-><init>(Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;Lcom/google/android/gms/common/api/internal/UnregisterListenerMethod;Ljava/lang/Runn...
    L225 [SDK/auth keyword] .method public register(Lcom/google/android/gms/common/api/internal/RemoteCall;)Lcom/google/android/gms/common/api/internal/RegistrationMethods$Builder;

FILE: smali\com\google\android\gms\common\api\internal\RegistrationMethods.smali
    L25 [SDK/auth keyword] .field public final register:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L25 [API route or URL] .field public final register:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L28 [API route or URL] "Lcom/google/android/gms/common/api/internal/RegisterListenerMethod<",
    L42 [API route or URL] .method synthetic constructor <init>(Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;Lcom/google/android/gms/common/api/internal/UnregisterListenerMethod;Ljava/lang/Runnable;Lcom/google/android/gms/common/api/internal/zacn;)V
    L47 [SDK/auth keyword] iput-object p1, p0, Lcom/google/android/gms/common/api/internal/RegistrationMethods;->register:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L47 [API route or URL] iput-object p1, p0, Lcom/google/android/gms/common/api/internal/RegistrationMethods;->register:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;

FILE: smali\com\google\android\gms\common\api\internal\zabb.smali
    L51 [SDK/auth keyword] invoke-static {v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->getInstance(Landroid/content/Context;)Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L51 [API route or URL] invoke-static {v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->getInstance(Landroid/content/Context;)Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L55 [SDK/auth keyword] invoke-virtual {v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac()V
    L55 [API route or URL] invoke-virtual {v0}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->zac()V

FILE: smali\com\google\android\gms\common\api\internal\zabq.smali
    L302 [server/config field] invoke-interface {v2}, Lcom/google/android/gms/common/api/Api$Client;->getEndpointPackageName()Ljava/lang/String;
    L552 [API route or URL] iget-object v2, v1, Lcom/google/android/gms/common/api/internal/zaci;->zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L554 [API route or URL] invoke-virtual {v2}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->getRequiredFeatures()[Lcom/google/android/gms/common/Feature;
    L572 [API route or URL] iget-object v1, v1, Lcom/google/android/gms/common/api/internal/zaci;->zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L580 [API route or URL] invoke-virtual {v1, v2, v3}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->registerListener(Lcom/google/android/gms/common/api/Api$AnyClient;Lcom/google/android/gms/tasks/TaskCompletionSource;)V
    L601 [SDK/auth keyword] const-string v1, "DeadObjectException thrown while calling register listener method."

FILE: smali\com\google\android\gms\common\api\internal\zaci.smali
    L7 [API route or URL] .field public final zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L15 [API route or URL] .method public constructor <init>(Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;Lcom/google/android/gms/common/api/internal/UnregisterListenerMethod;Ljava/lang/Runnable;)V
    L20 [API route or URL] iput-object p1, p0, Lcom/google/android/gms/common/api/internal/zaci;->zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;

FILE: smali\com\google\android\gms\common\api\internal\zack.smali
    L2 [API route or URL] .super Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L17 [API route or URL] invoke-direct {p0, p2, p3, p4, p5}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;-><init>(Lcom/google/android/gms/common/api/internal/ListenerHolder;[Lcom/google/android/gms/common/Feature;ZI)V

FILE: smali\com\google\android\gms\common\api\internal\zaf.smali
    L32 [API route or URL] iget-object p1, p1, Lcom/google/android/gms/common/api/internal/zaci;->zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L34 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zab()Z
    L47 [API route or URL] iget-object p1, p1, Lcom/google/android/gms/common/api/internal/zaci;->zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L49 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->getRequiredFeatures()[Lcom/google/android/gms/common/Feature;
    L67 [API route or URL] iget-object v0, v0, Lcom/google/android/gms/common/api/internal/zaci;->zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L75 [API route or URL] invoke-virtual {v0, v1, v2}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->registerListener(Lcom/google/android/gms/common/api/Api$AnyClient;Lcom/google/android/gms/tasks/TaskCompletionSource;)V
    L79 [API route or URL] iget-object v0, v0, Lcom/google/android/gms/common/api/internal/zaci;->zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L82 [API route or URL] invoke-virtual {v0}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->getListenerKey()Lcom/google/android/gms/common/api/internal/ListenerHolder$ListenerKey;

FILE: smali\com\google\android\gms\common\api\internal\zah.smali
    L44 [API route or URL] iget-object p1, p1, Lcom/google/android/gms/common/api/internal/zaci;->zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L47 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->zab()Z
    L86 [API route or URL] iget-object p1, p1, Lcom/google/android/gms/common/api/internal/zaci;->zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L89 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->getRequiredFeatures()[Lcom/google/android/gms/common/Feature;
    L130 [API route or URL] iget-object p1, v0, Lcom/google/android/gms/common/api/internal/zaci;->zaa:Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;
    L133 [API route or URL] invoke-virtual {p1}, Lcom/google/android/gms/common/api/internal/RegisterListenerMethod;->clearListener()V

FILE: smali\com\google\android\gms\common\api\internal\zap.smali
    L325 [identity/device field] const-string v2, "failed_client_id"
    L379 [identity/device field] const-string v1, "failed_client_id"

FILE: smali\com\google\android\gms\common\FirstPartyScopes.smali
    L7 [SDK/auth keyword] .field public static final GAMES_1P:Ljava/lang/String; = "https://www.googleapis.com/auth/games.firstparty"
    L7 [API route or URL] .field public static final GAMES_1P:Ljava/lang/String; = "https://www.googleapis.com/auth/games.firstparty"

FILE: smali\com\google\android\gms\common\GoogleApiAvailabilityLight.smali
    L209 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L228 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\common\GooglePlayServicesUtilLight.smali
    L257 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L531 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L627 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L892 [identity/device field] .method public static isGooglePlayServicesUid(Landroid/content/Context;I)Z
    L898 [identity/device field] invoke-static {p0, p1}, Lcom/google/android/gms/common/util/UidVerifier;->isGooglePlayServicesUid(Landroid/content/Context;I)Z
    L981 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L1058 [identity/device field] .method public static uidHasPackageName(Landroid/content/Context;ILjava/lang/String;)Z
    L1058 [server/config field] .method public static uidHasPackageName(Landroid/content/Context;ILjava/lang/String;)Z
    L1064 [identity/device field] invoke-static {p0, p1, p2}, Lcom/google/android/gms/common/util/UidVerifier;->uidHasPackageName(Landroid/content/Context;ILjava/lang/String;)Z
    L1064 [server/config field] invoke-static {p0, p1, p2}, Lcom/google/android/gms/common/util/UidVerifier;->uidHasPackageName(Landroid/content/Context;ILjava/lang/String;)Z
    L1126 [server/config field] invoke-virtual {v4}, Landroid/content/pm/PackageInstaller$SessionInfo;->getAppPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\common\GoogleSignatureVerifier.smali
    L190 [server/config field] iget-object v3, p0, Landroid/content/pm/PackageInfo;->packageName:Ljava/lang/String;
    L199 [server/config field] iget-object v2, p0, Landroid/content/pm/PackageInfo;->packageName:Ljava/lang/String;
    L398 [server/config field] iget-object v3, p3, Landroid/content/pm/PackageInfo;->packageName:Ljava/lang/String;
    L564 [identity/device field] .method public isUidGoogleSigned(I)Z
    L574 [identity/device field] invoke-virtual {v0, p1}, Landroid/content/pm/PackageManager;->getPackagesForUid(I)[Ljava/lang/String;

FILE: smali\com\google\android\gms\common\internal\BaseGmsClient.smali
    L816 [server/config field] invoke-virtual {v4}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L1772 [server/config field] .method public getEndpointPackageName()Ljava/lang/String;
    L1930 [server/config field] invoke-virtual {v3}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\common\internal\ClientIdentity.smali
    L1 [identity/device field] .class public Lcom/google/android/gms/common/internal/ClientIdentity;
    L11 [identity/device field] "Lcom/google/android/gms/common/internal/ClientIdentity;",
    L19 [server/config field] .field public final packageName:Ljava/lang/String;
    L21 [identity/device field] .field public final uid:I
    L32 [identity/device field] sput-object v0, Lcom/google/android/gms/common/internal/ClientIdentity;->CREATOR:Landroid/os/Parcelable$Creator;
    L43 [identity/device field] iput p1, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->uid:I
    L45 [identity/device field] iput-object p2, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->packageName:Ljava/lang/String;
    L45 [server/config field] iput-object p2, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->packageName:Ljava/lang/String;
    L63 [identity/device field] instance-of v1, p1, Lcom/google/android/gms/common/internal/ClientIdentity;
    L72 [identity/device field] check-cast p1, Lcom/google/android/gms/common/internal/ClientIdentity;
    L75 [identity/device field] iget v1, p1, Lcom/google/android/gms/common/internal/ClientIdentity;->uid:I
    L77 [identity/device field] iget v3, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->uid:I
    L81 [identity/device field] iget-object p1, p1, Lcom/google/android/gms/common/internal/ClientIdentity;->packageName:Ljava/lang/String;
    L81 [server/config field] iget-object p1, p1, Lcom/google/android/gms/common/internal/ClientIdentity;->packageName:Ljava/lang/String;
    L83 [identity/device field] iget-object v1, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->packageName:Ljava/lang/String;
    L83 [server/config field] iget-object v1, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->packageName:Ljava/lang/String;
    L100 [identity/device field] iget v0, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->uid:I
    L113 [identity/device field] iget v1, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->uid:I
    L121 [identity/device field] iget-object v1, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->packageName:Ljava/lang/String;
    L121 [server/config field] iget-object v1, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->packageName:Ljava/lang/String;
    L136 [identity/device field] iget p2, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->uid:I
    L147 [identity/device field] iget-object p2, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->packageName:Ljava/lang/String;
    L147 [server/config field] iget-object p2, p0, Lcom/google/android/gms/common/internal/ClientIdentity;->packageName:Ljava/lang/String;

FILE: smali\com\google\android\gms\common\internal\ClientSettings$Builder.smali
    L78 [server/config field] .method public setRealClientPackageName(Ljava/lang/String;)Lcom/google/android/gms/common/internal/ClientSettings$Builder;

FILE: smali\com\google\android\gms\common\internal\ClientSettings.smali
    L354 [server/config field] .method public getRealClientPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\common\internal\ServiceSpecificExtraArgs$GamesExtraArgs.smali
    L20 [server/config field] .field public static final GAME_PACKAGE_NAME:Ljava/lang/String; = "com.google.android.gms.games.key.gamePackageName"

FILE: smali\com\google\android\gms\common\internal\StringResourceValueReader.smali
    L32 [server/config field] invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getResourcePackageName(I)Ljava/lang/String;

FILE: smali\com\google\android\gms\common\internal\ViewUtils.smali
    L52 [server/config field] invoke-virtual {p2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\common\internal\zaa.smali
    L84 [identity/device field] new-instance p1, Lcom/google/android/gms/common/internal/ClientIdentity;
    L86 [identity/device field] invoke-direct {p1, v2, v1}, Lcom/google/android/gms/common/internal/ClientIdentity;-><init>(ILjava/lang/String;)V
    L95 [identity/device field] new-array p1, p1, [Lcom/google/android/gms/common/internal/ClientIdentity;

FILE: smali\com\google\android\gms\common\internal\zac.smali
    L30 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\common\internal\zat.smali
    L25 [SDK/auth keyword] .field private final zad:Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L25 [API route or URL] .field private final zad:Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L41 [SDK/auth keyword] .method constructor <init>(ILandroid/accounts/Account;ILcom/google/android/gms/auth/api/signin/GoogleSignInAccount;)V
    L41 [API route or URL] .method constructor <init>(ILandroid/accounts/Account;ILcom/google/android/gms/auth/api/signin/GoogleSignInAccount;)V
    L53 [SDK/auth keyword] iput-object p4, p0, Lcom/google/android/gms/common/internal/zat;->zad:Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L53 [API route or URL] iput-object p4, p0, Lcom/google/android/gms/common/internal/zat;->zad:Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L58 [SDK/auth keyword] .method public constructor <init>(Landroid/accounts/Account;ILcom/google/android/gms/auth/api/signin/GoogleSignInAccount;)V
    L58 [API route or URL] .method public constructor <init>(Landroid/accounts/Account;ILcom/google/android/gms/auth/api/signin/GoogleSignInAccount;)V
    L64 [SDK/auth keyword] invoke-direct {p0, v0, p1, p2, p3}, Lcom/google/android/gms/common/internal/zat;-><init>(ILandroid/accounts/Account;ILcom/google/android/gms/auth/api/signin/GoogleSignInAccount;)V
    L64 [API route or URL] invoke-direct {p0, v0, p1, p2, p3}, Lcom/google/android/gms/common/internal/zat;-><init>(ILandroid/accounts/Account;ILcom/google/android/gms/auth/api/signin/GoogleSignInAccount;)V
    L104 [SDK/auth keyword] iget-object v2, p0, Lcom/google/android/gms/common/internal/zat;->zad:Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L104 [API route or URL] iget-object v2, p0, Lcom/google/android/gms/common/internal/zat;->zad:Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;

FILE: smali\com\google\android\gms\common\internal\zau.smali
    L79 [SDK/auth keyword] sget-object v2, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->CREATOR:Landroid/os/Parcelable$Creator;
    L79 [API route or URL] sget-object v2, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->CREATOR:Landroid/os/Parcelable$Creator;
    L86 [SDK/auth keyword] check-cast v2, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L86 [API route or URL] check-cast v2, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L125 [SDK/auth keyword] invoke-direct {p1, v3, v1, v4, v2}, Lcom/google/android/gms/common/internal/zat;-><init>(ILandroid/accounts/Account;ILcom/google/android/gms/auth/api/signin/GoogleSignInAccount;)V
    L125 [API route or URL] invoke-direct {p1, v3, v1, v4, v2}, Lcom/google/android/gms/common/internal/zat;-><init>(ILandroid/accounts/Account;ILcom/google/android/gms/auth/api/signin/GoogleSignInAccount;)V

FILE: smali\com\google\android\gms\common\internal\zzah.smali
    L74 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\common\internal\zzu.smali
    L16 [API route or URL] const-string v0, "https://plus.google.com/"

FILE: smali\com\google\android\gms\common\moduleinstall\internal\zay.smali
    L565 [SDK/auth keyword] invoke-virtual {v1, v10}, Lcom/google/android/gms/common/api/internal/RegistrationMethods$Builder;->register(Lcom/google/android/gms/common/api/internal/RemoteCall;)Lcom/google/android/gms/common/api/internal/RegistrationMethods$Builder;

FILE: smali\com\google\android\gms\common\moduleinstall\ModuleInstallResponse.smali
    L80 [identity/device field] .method public getSessionId()I
    L99 [identity/device field] invoke-virtual {p0}, Lcom/google/android/gms/common/moduleinstall/ModuleInstallResponse;->getSessionId()I

FILE: smali\com\google\android\gms\common\moduleinstall\ModuleInstallStatusUpdate.smali
    L135 [identity/device field] .method public getSessionId()I
    L154 [identity/device field] invoke-virtual {p0}, Lcom/google/android/gms/common/moduleinstall/ModuleInstallStatusUpdate;->getSessionId()I

FILE: smali\com\google\android\gms\common\Scopes.smali
    L7 [SDK/auth keyword] .field public static final APP_STATE:Ljava/lang/String; = "https://www.googleapis.com/auth/appstate"
    L7 [API route or URL] .field public static final APP_STATE:Ljava/lang/String; = "https://www.googleapis.com/auth/appstate"
    L9 [SDK/auth keyword] .field public static final CLOUD_SAVE:Ljava/lang/String; = "https://www.googleapis.com/auth/datastoremobile"
    L9 [API route or URL] .field public static final CLOUD_SAVE:Ljava/lang/String; = "https://www.googleapis.com/auth/datastoremobile"
    L11 [SDK/auth keyword] .field public static final DRIVE_APPFOLDER:Ljava/lang/String; = "https://www.googleapis.com/auth/drive.appdata"
    L11 [API route or URL] .field public static final DRIVE_APPFOLDER:Ljava/lang/String; = "https://www.googleapis.com/auth/drive.appdata"
    L13 [SDK/auth keyword] .field public static final DRIVE_APPS:Ljava/lang/String; = "https://www.googleapis.com/auth/drive.apps"
    L13 [API route or URL] .field public static final DRIVE_APPS:Ljava/lang/String; = "https://www.googleapis.com/auth/drive.apps"
    L15 [SDK/auth keyword] .field public static final DRIVE_FILE:Ljava/lang/String; = "https://www.googleapis.com/auth/drive.file"
    L15 [API route or URL] .field public static final DRIVE_FILE:Ljava/lang/String; = "https://www.googleapis.com/auth/drive.file"
    L17 [SDK/auth keyword] .field public static final DRIVE_FULL:Ljava/lang/String; = "https://www.googleapis.com/auth/drive"
    L17 [API route or URL] .field public static final DRIVE_FULL:Ljava/lang/String; = "https://www.googleapis.com/auth/drive"
    L21 [SDK/auth keyword] .field public static final GAMES:Ljava/lang/String; = "https://www.googleapis.com/auth/games"
    L21 [API route or URL] .field public static final GAMES:Ljava/lang/String; = "https://www.googleapis.com/auth/games"
    L23 [SDK/auth keyword] .field public static final GAMES_LITE:Ljava/lang/String; = "https://www.googleapis.com/auth/games_lite"
    L23 [API route or URL] .field public static final GAMES_LITE:Ljava/lang/String; = "https://www.googleapis.com/auth/games_lite"
    L25 [SDK/auth keyword] .field public static final LEGACY_USERINFO_EMAIL:<redacted>; = "https://www.googleapis.com/auth/userinfo.email"
    L25 [API route or URL] .field public static final LEGACY_USERINFO_EMAIL:<redacted>; = "https://www.googleapis.com/auth/userinfo.email"
    L27 [SDK/auth keyword] .field public static final LEGACY_USERINFO_PROFILE:Ljava/lang/String; = "https://www.googleapis.com/auth/userinfo.profile"
    L27 [API route or URL] .field public static final LEGACY_USERINFO_PROFILE:Ljava/lang/String; = "https://www.googleapis.com/auth/userinfo.profile"
    L31 [SDK/auth keyword] .field public static final PLUS_LOGIN:Ljava/lang/String; = "https://www.googleapis.com/auth/plus.login"
    L31 [API route or URL] .field public static final PLUS_LOGIN:Ljava/lang/String; = "https://www.googleapis.com/auth/plus.login"
    L36 [SDK/auth keyword] .field public static final PLUS_ME:Ljava/lang/String; = "https://www.googleapis.com/auth/plus.me"
    L36 [API route or URL] .field public static final PLUS_ME:Ljava/lang/String; = "https://www.googleapis.com/auth/plus.me"

FILE: smali\com\google\android\gms\common\server\response\FastParser.smali
    L1361 [SDK/auth keyword] const-string v2, "Unexpected token: <redacted>
    L1459 [SDK/auth keyword] const-string v2, "Unexpected token "
    L2062 [SDK/auth keyword] const-string v5, "Unexpected token: <redacted>
    L2450 [SDK/auth keyword] const-string v1, "Unexpected token: <redacted>
    L3332 [SDK/auth keyword] const-string v2, "Unexpected token: <redacted>

FILE: smali\com\google\android\gms\common\stats\ConnectionTracker.smali
    L132 [server/config field] invoke-virtual {p6}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\common\util\UidVerifier.smali
    L1 [identity/device field] .class public final Lcom/google/android/gms/common/util/UidVerifier;
    L15 [identity/device field] .method public static isGooglePlayServicesUid(Landroid/content/Context;I)Z
    L21 [identity/device field] invoke-static {p0, p1, v0}, Lcom/google/android/gms/common/util/UidVerifier;->uidHasPackageName(Landroid/content/Context;ILjava/lang/String;)Z
    L21 [server/config field] invoke-static {p0, p1, v0}, Lcom/google/android/gms/common/util/UidVerifier;->uidHasPackageName(Landroid/content/Context;ILjava/lang/String;)Z
    L60 [identity/device field] const-string p1, "UidVerifier"
    L81 [identity/device field] .method public static uidHasPackageName(Landroid/content/Context;ILjava/lang/String;)Z
    L81 [server/config field] .method public static uidHasPackageName(Landroid/content/Context;ILjava/lang/String;)Z

FILE: smali\com\google\android\gms\common\util\WorkSourceUtil.smali
    L35 [identity/device field] invoke-static {}, Landroid/os/Process;->myUid()I
    L460 [identity/device field] iget p0, p0, Landroid/content/pm/ApplicationInfo;->uid:I
    L540 [identity/device field] iget v2, p0, Landroid/content/pm/ApplicationInfo;->uid:I

FILE: smali\com\google\android\gms\common\wrappers\PackageManagerWrapper.smali
    L208 [identity/device field] invoke-static {}, Landroid/os/Binder;->getCallingUid()I
    L212 [identity/device field] invoke-static {}, Landroid/os/Process;->myUid()I
    L241 [identity/device field] invoke-static {}, Landroid/os/Binder;->getCallingUid()I
    L245 [identity/device field] invoke-virtual {v0, v1}, Landroid/content/pm/PackageManager;->getNameForUid(I)Ljava/lang/String;
    L327 [identity/device field] invoke-virtual {v0, p1}, Landroid/content/pm/PackageManager;->getPackagesForUid(I)[Ljava/lang/String;

FILE: smali\com\google\android\gms\common\zzz.smali
    L178 [server/config field] const-string v1, "packageName must be defined"

FILE: smali\com\google\android\gms\dynamite\DynamiteModule.smali
    L2554 [server/config field] iget-object v4, v0, Landroid/content/pm/ProviderInfo;->packageName:Ljava/lang/String;

FILE: smali\com\google\android\gms\internal\location\zzav.smali
    L205 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\internal\location\zzaz.smali
    L807 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L895 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\google\android\gms\internal\location\zzba.smali
    L21 [identity/device field] "Lcom/google/android/gms/common/internal/ClientIdentity;",
    L35 [identity/device field] "Lcom/google/android/gms/common/internal/ClientIdentity;",
    L87 [identity/device field] "Lcom/google/android/gms/common/internal/ClientIdentity;",

FILE: smali\com\google\android\gms\internal\location\zzbb.smali
    L193 [identity/device field] sget-object v3, Lcom/google/android/gms/common/internal/ClientIdentity;->CREATOR:Landroid/os/Parcelable$Creator;

FILE: smali\com\google\android\gms\internal\location\zzj.smali
    L21 [identity/device field] "Lcom/google/android/gms/common/internal/ClientIdentity;",
    L37 [identity/device field] "Lcom/google/android/gms/common/internal/ClientIdentity;",
    L80 [identity/device field] "Lcom/google/android/gms/common/internal/ClientIdentity;",

FILE: smali\com\google\android\gms\internal\location\zzk.smali
    L91 [identity/device field] sget-object v2, Lcom/google/android/gms/common/internal/ClientIdentity;->CREATOR:Landroid/os/Parcelable$Creator;

FILE: smali\com\google\android\gms\location\ActivityTransitionRequest.smali
    L45 [identity/device field] "Lcom/google/android/gms/common/internal/ClientIdentity;",
    L102 [identity/device field] "Lcom/google/android/gms/common/internal/ClientIdentity;",

FILE: smali\com\google\android\gms\location\FusedLocationProviderClient.smali
    L117 [SDK/auth keyword] invoke-virtual {p1, v8}, Lcom/google/android/gms/common/api/internal/RegistrationMethods$Builder;->register(Lcom/google/android/gms/common/api/internal/RemoteCall;)Lcom/google/android/gms/common/api/internal/RegistrationMethods$Builder;

FILE: smali\com\google\android\gms\location\zzo.smali
    L96 [identity/device field] sget-object v3, Lcom/google/android/gms/common/internal/ClientIdentity;->CREATOR:Landroid/os/Parcelable$Creator;

FILE: smali\com\google\android\gms\signin\internal\SignInClientImpl.smali
    L100 [identity/device field] const-string p0, "com.google.android.gms.common.internal.ClientSettings.sessionId"
    L122 [identity/device field] const-string p0, "com.google.android.gms.signin.internal.serverClientId"
    L136 [identity/device field] const-string p0, "com.google.android.gms.signin.internal.forceCodeForRefreshToken"
    L146 [identity/device field] const-string p0, "com.google.android.gms.signin.internal.logSessionId"
    L151 [identity/device field] const-string p0, "com.google.android.gms.signin.internal.waitForAccessTokenRefresh"
    L206 [server/config field] invoke-virtual {v0}, Lcom/google/android/gms/common/internal/ClientSettings;->getRealClientPackageName()Ljava/lang/String;
    L215 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L229 [server/config field] const-string v2, "com.google.android.gms.signin.internal.realClientPackageName"
    L232 [server/config field] invoke-virtual {v1}, Lcom/google/android/gms/common/internal/ClientSettings;->getRealClientPackageName()Ljava/lang/String;
    L408 [SDK/auth keyword] invoke-static {v3}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->getInstance(Landroid/content/Context;)Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L408 [API route or URL] invoke-static {v3}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->getInstance(Landroid/content/Context;)Lcom/google/android/gms/auth/api/signin/internal/Storage;
    L412 [SDK/auth keyword] invoke-virtual {v3}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->getSavedDefaultGoogleSignInAccount()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L412 [API route or URL] invoke-virtual {v3}, Lcom/google/android/gms/auth/api/signin/internal/Storage;->getSavedDefaultGoogleSignInAccount()Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L437 [SDK/auth keyword] invoke-direct {v4, v2, v5, v3}, Lcom/google/android/gms/common/internal/zat;-><init>(Landroid/accounts/Account;ILcom/google/android/gms/auth/api/signin/GoogleSignInAccount;)V
    L437 [API route or URL] invoke-direct {v4, v2, v5, v3}, Lcom/google/android/gms/common/internal/zat;-><init>(Landroid/accounts/Account;ILcom/google/android/gms/auth/api/signin/GoogleSignInAccount;)V

FILE: smali\com\google\android\gms\signin\internal\zad.smali
    L82 [SDK/auth keyword] sget-object p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->CREATOR:Landroid/os/Parcelable$Creator;
    L82 [API route or URL] sget-object p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;->CREATOR:Landroid/os/Parcelable$Creator;
    L88 [SDK/auth keyword] check-cast p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;
    L88 [API route or URL] check-cast p1, Lcom/google/android/gms/auth/api/signin/GoogleSignInAccount;

FILE: smali\com\gosu\sdk\unity\SdkBridge.smali
    L1 [SDK/auth keyword] .class public Lcom/gosu/sdk/unity/SdkBridge;
    L1 [API route or URL] .class public Lcom/gosu/sdk/unity/SdkBridge;
    L62 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L62 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L81 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L81 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L104 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L104 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L113 [SDK/auth keyword] sput-object p0, Lcom/gosu/sdk/unity/SdkBridge;->mGameObjectName:Ljava/lang/String;
    L113 [API route or URL] sput-object p0, Lcom/gosu/sdk/unity/SdkBridge;->mGameObjectName:Ljava/lang/String;
    L116 [SDK/auth keyword] sput-object p1, Lcom/gosu/sdk/unity/SdkBridge;->mCallbackFunctionName:Ljava/lang/String;
    L116 [API route or URL] sput-object p1, Lcom/gosu/sdk/unity/SdkBridge;->mCallbackFunctionName:Ljava/lang/String;
    L137 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L137 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L142 [SDK/auth keyword] .method public static Login()V
    L149 [SDK/auth keyword] const-string v1, "Login"
    L152 [SDK/auth keyword] invoke-static {v1, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L152 [API route or URL] invoke-static {v1, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L157 [SDK/auth keyword] .method public static Logout()V
    L164 [SDK/auth keyword] const-string v1, "Logout"
    L167 [SDK/auth keyword] invoke-static {v1, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L167 [API route or URL] invoke-static {v1, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L214 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L214 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L233 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L233 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L284 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L284 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L315 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L315 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L338 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L338 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L361 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L361 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L370 [SDK/auth keyword] sget-object v0, Lcom/gosu/sdk/unity/SdkBridge;->mGameObjectName:Ljava/lang/String;
    L370 [API route or URL] sget-object v0, Lcom/gosu/sdk/unity/SdkBridge;->mGameObjectName:Ljava/lang/String;
    L404 [SDK/auth keyword] sget-object p1, Lcom/gosu/sdk/unity/SdkBridge;->mGameObjectName:Ljava/lang/String;
    L404 [API route or URL] sget-object p1, Lcom/gosu/sdk/unity/SdkBridge;->mGameObjectName:Ljava/lang/String;
    L406 [SDK/auth keyword] sget-object v0, Lcom/gosu/sdk/unity/SdkBridge;->mCallbackFunctionName:Ljava/lang/String;
    L406 [API route or URL] sget-object v0, Lcom/gosu/sdk/unity/SdkBridge;->mCallbackFunctionName:Ljava/lang/String;
    L511 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L511 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L526 [SDK/auth keyword] invoke-static {v1, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L526 [API route or URL] invoke-static {v1, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L535 [SDK/auth keyword] sput-object p0, Lcom/gosu/sdk/unity/SdkBridge;->mCallbackFunctionName:Ljava/lang/String;
    L535 [API route or URL] sput-object p0, Lcom/gosu/sdk/unity/SdkBridge;->mCallbackFunctionName:Ljava/lang/String;
    L548 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L548 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L557 [SDK/auth keyword] sput-object p0, Lcom/gosu/sdk/unity/SdkBridge;->mGameObjectName:Ljava/lang/String;
    L557 [API route or URL] sput-object p0, Lcom/gosu/sdk/unity/SdkBridge;->mGameObjectName:Ljava/lang/String;
    L570 [SDK/auth keyword] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V
    L570 [API route or URL] invoke-static {p0, v0}, Lcom/gosu/sdk/unity/SdkBridge;->forward(Ljava/lang/String;[Ljava/lang/String;)V

FILE: smali\com\unity3d\player\a\e.smali
    L38 [server/config field] invoke-virtual {p2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L65 [server/config field] invoke-virtual {p2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\unity3d\player\BuildConfig.smali
    L11 [server/config field] .field public static final LIBRARY_PACKAGE_NAME:Ljava/lang/String; = "com.unity3d.player"

FILE: smali\com\unity3d\player\f.1.smali
    L178 [HTTP/API client] invoke-interface {v4, v3}, Lcom/google/android/play/core/assetpacks/AssetPackManager;->fetch(Ljava/util/List;)Lcom/google/android/gms/tasks/Task;

FILE: smali\com\unity3d\player\m.1.smali
    L42 [SDK/auth keyword] const-string v0, "Camera2: Capture session failed "

FILE: smali\com\unity3d\player\M0.smali
    L308 [identity/device field] .method public getAudioSessionId()I
    L320 [identity/device field] invoke-virtual {v0}, Landroid/media/MediaPlayer;->getAudioSessionId()I

FILE: smali\com\unity3d\player\s.1.smali
    L44 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L84 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\unity3d\player\UnityPermissions.smali
    L158 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\unity3d\player\UnityPlayer.smali
    L873 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L1124 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L2861 [server/config field] invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L3128 [server/config field] invoke-virtual {v2}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\unity3d\player\Y.smali
    L62 [server/config field] invoke-virtual {p1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;
    L170 [server/config field] invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

FILE: smali\com\unity\purchasing\BuildConfig.smali
    L11 [server/config field] .field public static final LIBRARY_PACKAGE_NAME:Ljava/lang/String; = "com.unity.purchasing"

[3] SUGGESTED MANUAL REVIEW ORDER
------------------------------------------------------------------------------
1. AndroidManifest.xml: package, activities, permissions, exported components.
2. res/xml, assets, config JSON/XML: base URLs, app IDs, SDK switches.
3. smali*/... files whose names contain sdk/auth/login/network/request.
4. Java/Kotlin/C# wrappers and Unity networking code, if present.
5. Protobuf .proto files and model/serializer definitions, if present.
6. Compare endpoint strings with sanitized Fiddler captures and Flask logs.
