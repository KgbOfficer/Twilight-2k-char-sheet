"""
audio_manager.py - Audio management for the application
"""

import os
from PyQt6.QtCore import QUrl, QObject
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaDevices
import src.config as config

class AudioManager(QObject):
    """Manages audio playback for the application"""

    def __init__(self):
        super().__init__()

        # Set up audio output
        self.audio_output = QAudioOutput()
        self.audio_output.setVolume(config.MASTER_VOLUME)

        # Set up media player for background music
        self.music_player = QMediaPlayer()
        self.music_player.setAudioOutput(self.audio_output)

        # Set up media player for sound effects
        self.sfx_player = QMediaPlayer()
        self.sfx_output = QAudioOutput()
        self.sfx_output.setVolume(config.SFX_VOLUME)
        self.sfx_player.setAudioOutput(self.sfx_output)

        # Track currently playing music
        self.current_music = None

        # Check for available audio devices
        self._check_audio_devices()

    def _check_audio_devices(self):
        """Check for available audio devices"""
        devices = QMediaDevices.audioOutputs()
        if not devices:
            print("Warning: No audio output devices found")

    def play_music(self, music_key, loop=True):
        """Play background music

        Args:
            music_key: Key to audio file in config.AUDIO_FILES
            loop: Whether to loop the music
        """
        if not config.ENABLE_MUSIC:
            return

        if music_key not in config.AUDIO_FILES:
            print(f"Warning: Music key '{music_key}' not found in audio files")
            return

        # Get the music file path
        music_file = config.AUDIO_FILES[music_key]

        # Check if file exists
        if not os.path.exists(music_file):
            print(f"Warning: Music file '{music_file}' not found")
            return

        # Stop any currently playing music
        self.stop_music()

        # Set the source and play
        self.music_player.setSource(QUrl.fromLocalFile(music_file))
        self.music_player.play()

        # Set up looping if requested
        if loop:
            self.music_player.mediaStatusChanged.connect(self._on_music_status_changed)

        # Track the current music
        self.current_music = music_key

    def _on_music_status_changed(self, status):
        """Handle music player status changes for looping"""
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            # Restart the music from the beginning
            self.music_player.setPosition(0)
            self.music_player.play()

    def stop_music(self):
        """Stop currently playing music"""
        self.music_player.stop()

        # Disconnect any connected signals to avoid multiple connections
        try:
            self.music_player.mediaStatusChanged.disconnect()
        except TypeError:
            # No connections to disconnect
            pass

        self.current_music = None

    def play_sound(self, sound_key):
        """Play a sound effect

        Args:
            sound_key: Key to audio file in config.AUDIO_FILES
        """
        if not config.ENABLE_SFX:
            return

        if sound_key not in config.AUDIO_FILES:
            print(f"Warning: Sound key '{sound_key}' not found in audio files")
            return

        # Get the sound file path
        sound_file = config.AUDIO_FILES[sound_key]

        # Check if file exists
        if not os.path.exists(sound_file):
            print(f"Warning: Sound file '{sound_file}' not found")
            return

        # Set the source and play
        self.sfx_player.setSource(QUrl.fromLocalFile(sound_file))
        self.sfx_player.play()

    def set_master_volume(self, volume):
        """Set the master volume (0.0 to 1.0)"""
        self.audio_output.setVolume(volume)

    def set_sfx_volume(self, volume):
        """Set the sound effects volume (0.0 to 1.0)"""
        self.sfx_output.setVolume(volume)

    def enable_music(self, enable=True):
        """Enable or disable music"""
        config.ENABLE_MUSIC = enable
        if not enable:
            self.stop_music()

    def enable_sfx(self, enable=True):
        """Enable or disable sound effects"""
        config.ENABLE_SFX = enable

# Create a global instance for easy access
audio_manager = AudioManager()