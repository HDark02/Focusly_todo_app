import time
from jnius import autoclass


# ============================================================
# Android
# ============================================================

PythonService = autoclass("org.kivy.android.PythonService")
service = PythonService.mService

Context = autoclass("android.content.Context")

NotificationChannel = autoclass(
    "android.app.NotificationChannel"
)

NotificationManager = autoclass(
    "android.app.NotificationManager"
)

NotificationBuilder = autoclass(
    "android.app.Notification$Builder"
)

PendingIntent = autoclass(
    "android.app.PendingIntent"
)

Intent = autoclass(
    "android.content.Intent"
)

BuildVersion = autoclass(
    "android.os.Build$VERSION"
)

BuildCodes = autoclass(
    "android.os.Build$VERSION_CODES"
)

Uri = autoclass(
    "android.net.Uri"
)

R = autoclass(
    "android.R"
)


# ============================================================
# Configuration
# ============================================================

CHANNEL_ID = "focusly_notifications"
NOTIFICATION_ID = 1001


# ============================================================
# Création du canal
# ============================================================

def create_notification_channel():

    if BuildVersion.SDK_INT < 26:
        return

    notification_manager = service.getSystemService(
        Context.NOTIFICATION_SERVICE
    )

    channel = NotificationChannel(
        CHANNEL_ID,
        "Focusly",
        NotificationManager.IMPORTANCE_HIGH
    )

    channel.setDescription(
        "Notifications de rappel Focusly"
    )

    channel.enableVibration(True)

    channel.setVibrationPattern(
        [0, 500, 250, 500]
    )

    notification_manager.createNotificationChannel(
        channel
    )


# ============================================================
# Notification
# ============================================================

def send_notification():

    create_notification_channel()

    notification_manager = service.getSystemService(
        Context.NOTIFICATION_SERVICE
    )

    package_manager = service.getPackageManager()
    package_name = service.getPackageName()

    launch_intent = package_manager.getLaunchIntentForPackage(
        package_name
    )

    if launch_intent is None:
        print("Impossible de lancer Focusly")
        return

    launch_intent.setFlags(
        Intent.FLAG_ACTIVITY_NEW_TASK
        | Intent.FLAG_ACTIVITY_CLEAR_TOP
        | Intent.FLAG_ACTIVITY_SINGLE_TOP
    )

    flags = PendingIntent.FLAG_UPDATE_CURRENT

    if BuildVersion.SDK_INT >= 23:
        flags |= PendingIntent.FLAG_IMMUTABLE

    pending_intent = PendingIntent.getActivity(
        service,
        0,
        launch_intent,
        flags
    )

    # ========================================================
    # Builder
    # ========================================================

    if BuildVersion.SDK_INT >= 26:

        builder = NotificationBuilder(
            service,
            CHANNEL_ID
        )

    else:

        builder = NotificationBuilder(service)

        builder.setSound(
            Uri.parse(
                "content://settings/system/notification_sound"
            )
        )

        builder.setVibrate(
            [0, 500, 250, 500]
        )

    builder.setSmallIcon(
        R.drawable.ic_dialog_info
    )

    builder.setContentTitle(
        "⏰ Focusly"
    )

    builder.setContentText(
        "C'est le moment ! Ton rappel est arrivé."
    )

    BigTextStyle = autoclass(
        "android.app.Notification$BigTextStyle"
    )

    builder.setStyle(
        BigTextStyle().bigText(
            "Ton rappel Focusly est arrivé."
        )
    )

    builder.setContentIntent(
        pending_intent
    )

    builder.setAutoCancel(True)

    builder.setVibrate(
        [0, 500, 250, 500]
    )

    notification = builder.build()

    notification_manager.notify(
        NOTIFICATION_ID,
        notification
    )


# ============================================================
# Programme principal
# ============================================================

print("===================================")
print("Focusly Notification Service")
print("Service démarré")
print("===================================")


try:

    send_notification()

    print(
        "Notification Focusly envoyée !"
    )

except Exception as e:

    print(
        "Erreur notification :",
        e
    )


print("Service terminé.")